// SPDX-License-Identifier: GPL-3.0-or-later
#pragma once
#include <QApplication>
#include <QCheckBox>
#include <QFile>
#include <QJsonDocument>
#include <QJsonObject>
#include <QPainter>
#include <QPointer>
#include <QSettings>
#include <QSignalBlocker>
#include <QShowEvent>
#include <QTimer>
#include <QWindow>
#include <KWindowEffects>

// Only the navigation region is translucent; content and text retain full opacity.
class ProperMaterialWindow : public QWidget {
public:
    ProperMaterialWindow() {
        setAttribute(Qt::WA_TranslucentBackground);
        setProperty("materialWindow", true);
        QFile tokens("/usr/share/proper-linux/ui/proper-palette.json");
        if (tokens.open(QIODevice::ReadOnly))
            navigationOpacity = QJsonDocument::fromJson(tokens.readAll()).object()
                .value("opacity").toObject().value("application_navigation").toString().toDouble();
        navigationOpacity = qBound(0.75, navigationOpacity, 1.0);
        connect(&availability, &QTimer::timeout, this, [this] { updateMaterial(); });
        availability.setInterval(500);
    }
    void setNavigation(QWidget *widget) { navigation = widget; }
    QCheckBox *materialControl(QWidget *parent) {
        control = new QCheckBox("Translucent navigation", parent);
        control->setChecked(QSettings("ProperLinux", "Materials").value("translucentNavigation", true).toBool());
        connect(control, &QCheckBox::toggled, this, [this](bool checked) {
            QSettings("ProperLinux", "Materials").setValue("translucentNavigation", checked);
            updateMaterial();
        });
        return control;
    }
protected:
    void showEvent(QShowEvent *event) override {
        QWidget::showEvent(event);
        availability.start();
        updateMaterial();
    }
    void hideEvent(QHideEvent *event) override {
        availability.stop();
        QWidget::hideEvent(event);
    }
    void paintEvent(QPaintEvent *) override {
        QPainter painter(this);
        painter.setCompositionMode(QPainter::CompositionMode_Source);
        QColor colour = QApplication::palette().color(QPalette::Window);
        painter.fillRect(rect(), colour);
        colour.setAlphaF(frosted ? navigationOpacity : 1.0);
        painter.fillRect(navigationRect(), colour);
    }
private:
    QRect navigationRect() const {
        if (!navigation) return {};
        return QRect(navigation->mapTo(this, QPoint()), navigation->size());
    }
    bool requestedMaterial() {
        const bool requested = QSettings("ProperLinux", "Materials").value("translucentNavigation", true).toBool();
        if (control) {
            const QSignalBlocker blocker(control);
            control->setChecked(requested);
        }
        return requested;
    }
    void updateMaterial() {
        if (!windowHandle()) return;
        const bool enabled = requestedMaterial() && KWindowEffects::isEffectAvailable(KWindowEffects::BlurBehind);
        const QRect region = navigationRect();
        if (enabled == frosted && region == previousRegion) return;
        frosted = enabled;
        previousRegion = region;
        KWindowEffects::enableBlurBehind(windowHandle(), frosted, QRegion(region));
        update();
    }
    QPointer<QWidget> navigation;
    QPointer<QCheckBox> control;
    QTimer availability;
    QRect previousRegion;
    double navigationOpacity = 1.0;
    bool frosted = false;
};
