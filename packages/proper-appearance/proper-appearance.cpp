#include <QApplication>
#include <QButtonGroup>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QIcon>
#include <QLabel>
#include <QPainter>
#include <QProcess>
#include <QPushButton>
#include <QRegularExpression>
#include <QResizeEvent>
#include <QSaveFile>
#include <QScrollArea>
#include <QSettings>
#include <QStandardPaths>
#include <QToolButton>
#include <QVBoxLayout>
#include <QVector>

struct AppearanceVariant {
    QString id;
    QString name;
    QString description;
    QString wallpaperId;
    QString wallpaperPath;
    QColor base;
    QColor surface;
    QColor text;
    QColor accent;
};

struct Wallpaper {
    QString id;
    QString name;
    QString path;
};

struct TextPreset {
    QString id;
    QString name;
    QString description;
    int uiSize;
    int smallSize;
    int terminalSize;
};

static QString configRoot() {
    const QString root = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    return root.isEmpty() ? QDir::homePath() + "/.config" : root;
}

static QPixmap variantPreview(const AppearanceVariant &variant) {
    constexpr int width = 360;
    constexpr int height = 186;
    QPixmap preview(width, height);
    preview.fill(variant.base);

    QPainter painter(&preview);
    painter.setRenderHint(QPainter::Antialiasing);
    const QPixmap wallpaper(variant.wallpaperPath);
    if (!wallpaper.isNull()) {
        const QPixmap scaled = wallpaper.scaled(width, height, Qt::KeepAspectRatioByExpanding, Qt::SmoothTransformation);
        painter.drawPixmap(0, 0, scaled, (scaled.width() - width) / 2, (scaled.height() - height) / 2, width, height);
    }

    painter.setPen(Qt::NoPen);
    QColor panel = variant.surface;
    panel.setAlpha(205);
    painter.setBrush(panel);
    painter.drawRoundedRect(QRectF(54, 153, 252, 21), 10, 10);

    QColor window = variant.surface;
    window.setAlpha(245);
    painter.setBrush(window);
    painter.drawRoundedRect(QRectF(92, 24, 176, 113), 11, 11);
    painter.setBrush(variant.accent);
    painter.drawRoundedRect(QRectF(105, 38, 57, 7), 3.5, 3.5);
    QColor muted = variant.text;
    muted.setAlpha(105);
    painter.setBrush(muted);
    painter.drawRoundedRect(QRectF(105, 56, 110, 5), 2.5, 2.5);
    painter.drawRoundedRect(QRectF(105, 68, 86, 5), 2.5, 2.5);

    QColor terminal = variant.base;
    terminal.setAlpha(223);
    painter.setBrush(terminal);
    painter.drawRoundedRect(QRectF(105, 86, 149, 38), 7, 7);
    painter.setBrush(variant.accent);
    painter.drawRoundedRect(QRectF(117, 98, 53, 4), 2, 2);
    painter.setBrush(variant.text);
    painter.drawRoundedRect(QRectF(117, 108, 82, 4), 2, 2);
    return preview;
}

class ProperAppearance final : public QWidget {
public:
    ProperAppearance() {
        setWindowTitle("Appearance");
        setWindowIcon(QIcon::fromTheme("preferences-desktop-theme"));
        resize(1160, 820);
        setMinimumSize(760, 600);
        setStyleSheet(R"(
            QWidget { background: #11151d; color: #f1f4f8; }
            QScrollArea, QScrollArea > QWidget > QWidget { background: transparent; border: 0; }
            QLabel#subtitle, QLabel#sectionCopy, QLabel#status { color: #a8b2c2; }
            QLabel#sectionTitle { font-size: 19px; font-weight: 650; }
            QToolButton {
                background: rgba(27, 34, 45, 0.98);
                border: 1px solid rgba(168, 178, 194, 0.18);
                border-radius: 15px;
                color: rgba(241, 244, 248, 0.90);
                font-size: 14px;
                padding: 10px;
            }
            QToolButton:hover { background: #222c39; border-color: rgba(145, 180, 255, 0.44); }
            QToolButton:checked { background: #202c3d; border: 2px solid #91b4ff; color: white; }
            QToolButton#textPreset { min-height: 54px; text-align: left; padding: 8px 14px; }
            QPushButton {
                background: #253243;
                border: 1px solid rgba(168, 178, 194, 0.20);
                border-radius: 10px;
                color: white;
                min-height: 38px;
                padding: 0 18px;
                font-weight: 600;
            }
            QPushButton:hover { background: #304156; }
            QPushButton#primary { background: #91b4ff; border-color: #a9c5ff; color: #11151d; }
            QPushButton#primary:hover { background: #a9c5ff; }
        )");

        variants = {
            {"com.properlinux.dark.desktop", "Blue Hour", "Balanced dark · Proper default", "ProperBlueHour",
             "/usr/share/wallpapers/ProperBlueHour/contents/images/1920x1080.png", "#11151d", "#1b222d", "#f1f4f8", "#91b4ff"},
            {"com.properlinux.light.desktop", "Horizon Light", "Quiet light surfaces · dark shell", "ProperHorizon",
             "/usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png", "#f6f7fb", "#ffffff", "#18202b", "#3b68d9"},
            {"com.properlinux.midnight.desktop", "Midnight", "Deeper contrast · cool blue focus", "summer_1am",
             "/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg", "#090d14", "#141b25", "#f5f7fa", "#79a8ff"},
        };
        wallpapers = {
            {"ProperBlueHour", "Proper Blue Hour", "/usr/share/wallpapers/ProperBlueHour/contents/images/1920x1080.png"},
            {"ProperHorizon", "Proper Horizon", "/usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png"},
            {"Path", "Path", "/usr/share/wallpapers/Path/contents/images/2560x1600.jpg"},
            {"Volna", "Volna", "/usr/share/wallpapers/Volna/contents/images/5120x2880.jpg"},
            {"summer_1am", "Summer 1 AM", "/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg"},
        };
        textPresets = {
            {"compact", "Compact", "More room", 9, 8, 11},
            {"standard", "Standard", "Proper default", 10, 9, 12},
            {"large", "Large", "Easier to read", 12, 10, 14},
        };

        auto *outer = new QVBoxLayout(this);
        outer->setContentsMargins(28, 24, 28, 22);
        outer->setSpacing(14);

        auto *title = new QLabel("Appearance");
        QFont titleFont = title->font();
        titleFont.setPixelSize(28);
        titleFont.setBold(true);
        title->setFont(titleFont);
        outer->addWidget(title);
        auto *intro = new QLabel("A small set of coherent looks. Preview first; nothing changes until you apply it.");
        intro->setObjectName("subtitle");
        outer->addWidget(intro);

        auto *scroll = new QScrollArea;
        scroll->setWidgetResizable(true);
        scroll->setFrameShape(QFrame::NoFrame);
        auto *content = new QWidget;
        auto *root = new QVBoxLayout(content);
        root->setContentsMargins(0, 4, 0, 4);
        root->setSpacing(12);

        addSectionHeading(root, "Desktop style", "Colour, wallpaper, icons, and the Proper shell move together.");
        variantGroup = new QButtonGroup(this);
        variantGroup->setExclusive(true);
        variantGrid = new QGridLayout;
        variantGrid->setSpacing(16);
        for (int index = 0; index < variants.size(); ++index) {
            const auto &variant = variants[index];
            auto *card = new QToolButton;
            card->setText(variant.name + "\n" + variant.description);
            card->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
            card->setCheckable(true);
            card->setMinimumSize(300, 242);
            card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            card->setIcon(QIcon(variantPreview(variant)));
            card->setIconSize(QSize(320, 165));
            card->setAccessibleName(variant.name + ". " + variant.description);
            variantGroup->addButton(card, index);
            variantCards.append(card);
            variantGrid->addWidget(card, 0, index);
        }
        root->addLayout(variantGrid);
        auto *variantActions = new QHBoxLayout;
        variantStatus = new QLabel("Select a preview, then apply it.");
        variantStatus->setObjectName("status");
        variantStatus->setWordWrap(true);
        variantActions->addWidget(variantStatus, 1);
        auto *applyVariantButton = new QPushButton("Use desktop style");
        applyVariantButton->setObjectName("primary");
        variantActions->addWidget(applyVariantButton);
        root->addLayout(variantActions);

        addSectionHeading(root, "Text size", "One choice coordinates Plasma, GTK apps, and new Ghostty windows.");
        textGroup = new QButtonGroup(this);
        textGroup->setExclusive(true);
        auto *textRow = new QHBoxLayout;
        textRow->setSpacing(12);
        for (int index = 0; index < textPresets.size(); ++index) {
            const auto &preset = textPresets[index];
            auto *button = new QToolButton;
            button->setObjectName("textPreset");
            button->setText(preset.name + "\n" + preset.description);
            button->setCheckable(true);
            button->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            textGroup->addButton(button, index);
            textRow->addWidget(button);
        }
        auto *applyTextButton = new QPushButton("Use text size");
        textRow->addWidget(applyTextButton);
        root->addLayout(textRow);

        addSectionHeading(root, "Wallpapers", "Change only the desktop and lock-screen background, or sync the login screen too.");
        wallpaperGroup = new QButtonGroup(this);
        wallpaperGroup->setExclusive(true);
        wallpaperGrid = new QGridLayout;
        wallpaperGrid->setHorizontalSpacing(18);
        wallpaperGrid->setVerticalSpacing(18);
        for (int index = 0; index < wallpapers.size(); ++index) {
            const auto &wallpaper = wallpapers[index];
            auto *card = new QToolButton;
            card->setText(wallpaper.name);
            card->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
            card->setCheckable(true);
            card->setMinimumSize(260, 176);
            card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            card->setIconSize(QSize(280, 138));
            if (QFileInfo::exists(wallpaper.path)) card->setIcon(QIcon(wallpaper.path));
            wallpaperGroup->addButton(card, index);
            wallpaperCards.append(card);
        }
        root->addLayout(wallpaperGrid);

        auto *wallpaperActions = new QHBoxLayout;
        wallpaperStatus = new QLabel("Desktop and lock screen change together. Login sync asks for administrator approval.");
        wallpaperStatus->setObjectName("status");
        wallpaperStatus->setWordWrap(true);
        wallpaperActions->addWidget(wallpaperStatus, 1);
        auto *applyWallpaperButton = new QPushButton("Use wallpaper");
        auto *everywhereButton = new QPushButton("Use everywhere");
        everywhereButton->setObjectName("primary");
        everywhereButton->setIcon(QIcon::fromTheme("security-high"));
        wallpaperActions->addWidget(applyWallpaperButton);
        wallpaperActions->addWidget(everywhereButton);
        root->addLayout(wallpaperActions);
        root->addStretch();

        scroll->setWidget(content);
        outer->addWidget(scroll, 1);

        QSettings preferences(configRoot() + "/proper-linux/appearance.ini", QSettings::IniFormat);
        const QString selectedVariant = preferences.value("Appearance/variant", variants.first().id).toString();
        int variantIndex = 0;
        for (int index = 0; index < variants.size(); ++index)
            if (variants[index].id == selectedVariant) variantIndex = index;
        variantCards[variantIndex]->setChecked(true);
        wallpaperCards.first()->setChecked(true);
        const QString selectedText = preferences.value("Appearance/textSize", "standard").toString();
        int textIndex = 1;
        for (int index = 0; index < textPresets.size(); ++index)
            if (textPresets[index].id == selectedText) textIndex = index;
        textGroup->button(textIndex)->setChecked(true);
        rebuildVariantGrid(width());
        rebuildWallpaperGrid(width());

        connect(variantGroup, &QButtonGroup::idClicked, this, [this](int index) {
            if (index >= 0 && index < variants.size())
                variantStatus->setText(variants[index].name + " is selected for preview. Your desktop has not changed.");
        });
        connect(applyVariantButton, &QPushButton::clicked, this, [this] { applyVariant(); });
        connect(applyTextButton, &QPushButton::clicked, this, [this] { applyTextPreset(); });
        connect(applyWallpaperButton, &QPushButton::clicked, this, [this] { applyWallpaper(false); });
        connect(everywhereButton, &QPushButton::clicked, this, [this] { applyWallpaper(true); });
    }

protected:
    void resizeEvent(QResizeEvent *event) override {
        QWidget::resizeEvent(event);
        rebuildVariantGrid(event->size().width());
        rebuildWallpaperGrid(event->size().width());
    }

private:
    static void addSectionHeading(QVBoxLayout *layout, const QString &title, const QString &copy) {
        auto *heading = new QLabel(title);
        heading->setObjectName("sectionTitle");
        layout->addSpacing(8);
        layout->addWidget(heading);
        auto *description = new QLabel(copy);
        description->setObjectName("sectionCopy");
        description->setWordWrap(true);
        layout->addWidget(description);
    }

    void rebuildWallpaperGrid(int width) {
        const int wanted = width >= 1020 ? 3 : width >= 700 ? 2 : 1;
        if (wanted == wallpaperColumns && wallpaperGrid->count() == wallpaperCards.size()) return;
        wallpaperColumns = wanted;
        while (auto *item = wallpaperGrid->takeAt(0)) delete item;
        for (int index = 0; index < wallpaperCards.size(); ++index)
            wallpaperGrid->addWidget(wallpaperCards[index], index / wallpaperColumns, index % wallpaperColumns);
    }

    void rebuildVariantGrid(int width) {
        const int wanted = width >= 1040 ? 3 : width >= 700 ? 2 : 1;
        if (wanted == variantColumns && variantGrid->count() == variantCards.size()) return;
        variantColumns = wanted;
        while (auto *item = variantGrid->takeAt(0)) delete item;
        for (int index = 0; index < variantCards.size(); ++index)
            variantGrid->addWidget(variantCards[index], index / variantColumns, index % variantColumns);
    }

    static QString lookAndFeelTool() {
        QString tool = QStandardPaths::findExecutable("plasma-apply-lookandfeel");
        if (tool.isEmpty()) tool = QStandardPaths::findExecutable("lookandfeeltool");
        return tool;
    }

    void applyVariant() {
        const int index = variantGroup->checkedId();
        if (index < 0 || index >= variants.size()) return;
        const auto &variant = variants[index];
        const QString tool = lookAndFeelTool();
        if (tool.isEmpty()) {
            variantStatus->setText("The Plasma appearance tool is missing. Reinstall plasma-workspace and try again.");
            return;
        }
        if (QProcess::execute(tool, {"-a", variant.id}) != 0) {
            variantStatus->setText("That desktop style could not be applied. Your previous style is unchanged.");
            return;
        }
        if (QFileInfo::exists(variant.wallpaperPath))
            QProcess::execute("/usr/bin/plasma-apply-wallpaperimage", {variant.wallpaperPath});
        QSettings preferences(configRoot() + "/proper-linux/appearance.ini", QSettings::IniFormat);
        preferences.setValue("Appearance/variant", variant.id);
        variantStatus->setText(variant.name + " is now active. Open apps keep their current palette until restarted.");
    }

    static bool runConfigWrite(const QString &group, const QString &key, const QString &value) {
        const QString tool = QStandardPaths::findExecutable("kwriteconfig6");
        return !tool.isEmpty() && QProcess::execute(tool, {"--file", "kdeglobals", "--group", group, "--key", key, value}) == 0;
    }

    static bool writeGhosttyFont(int size) {
        const QString ghosttyDirectory = configRoot() + "/ghostty";
        if (!QDir().mkpath(ghosttyDirectory)) return false;
        const QString configPath = ghosttyDirectory + "/config";
        QFile existing(configPath);
        QByteArray contents;
        if (existing.exists()) {
            if (!existing.open(QIODevice::ReadOnly)) return false;
            contents = existing.readAll();
        }
        QStringList lines = QString::fromUtf8(contents).split('\n');
        const QRegularExpression activeFont("^\\s*font-size\\s*=");
        QStringList updatedLines;
        bool replaced = false;
        for (const QString &line : lines) {
            if (activeFont.match(line).hasMatch()) {
                if (!replaced) updatedLines << QString("font-size = %1").arg(size);
                replaced = true;
            } else {
                updatedLines << line;
            }
        }
        if (!replaced) updatedLines << QString("font-size = %1").arg(size);
        QSaveFile updated(configPath);
        if (!updated.open(QIODevice::WriteOnly | QIODevice::Text)) return false;
        updated.write(updatedLines.join('\n').toUtf8());
        return updated.commit();
    }

    static void writeGtkFont(const QString &path, int size) {
        QDir().mkpath(QFileInfo(path).absolutePath());
        QSettings settings(path, QSettings::IniFormat);
        settings.beginGroup("Settings");
        settings.setValue("gtk-font-name", QString("Noto Sans %1").arg(size));
        settings.endGroup();
        settings.sync();
    }

    void applyTextPreset() {
        const int index = textGroup->checkedId();
        if (index < 0 || index >= textPresets.size()) return;
        const auto &preset = textPresets[index];
        const QString normal = QString("Noto Sans,%1,-1,5,50,0,0,0,0,0").arg(preset.uiSize);
        const QString small = QString("Noto Sans,%1,-1,5,50,0,0,0,0,0").arg(preset.smallSize);
        bool ok = true;
        for (const QString &key : {QString("font"), QString("menuFont"), QString("toolBarFont")})
            ok = runConfigWrite("General", key, normal) && ok;
        ok = runConfigWrite("General", "smallestReadableFont", small) && ok;
        ok = writeGhosttyFont(preset.terminalSize) && ok;
        writeGtkFont(configRoot() + "/gtk-3.0/settings.ini", preset.uiSize);
        writeGtkFont(configRoot() + "/gtk-4.0/settings.ini", preset.uiSize);
        if (!ok) {
            variantStatus->setText("Text size could not be fully applied. Check that Plasma and your config folder are writable.");
            return;
        }
        QSettings preferences(configRoot() + "/proper-linux/appearance.ini", QSettings::IniFormat);
        preferences.setValue("Appearance/textSize", preset.id);
        const QString qdbus = QStandardPaths::findExecutable("qdbus-qt6");
        if (!qdbus.isEmpty())
            QProcess::startDetached(qdbus, {"org.kde.KGlobalSettings", "/KGlobalSettings", "org.kde.KGlobalSettings.notifyChange", "0", "0"});
        variantStatus->setText(preset.name + " text is set. Running apps may need to be reopened; new Ghostty windows use it immediately.");
    }

    void applyWallpaper(bool syncLogin) {
        const int index = wallpaperGroup->checkedId();
        if (index < 0 || index >= wallpapers.size()) return;
        const auto &wallpaper = wallpapers[index];
        if (!QFileInfo::exists(wallpaper.path)) {
            wallpaperStatus->setText("That wallpaper is missing. Reinstall Proper Linux artwork and try again.");
            return;
        }
        if (QProcess::execute("/usr/bin/plasma-apply-wallpaperimage", {wallpaper.path}) != 0) {
            wallpaperStatus->setText("The wallpaper could not be applied. Your previous wallpaper is unchanged.");
            return;
        }
        wallpaperStatus->setText(wallpaper.name + " now appears on the desktop and lock screen.");
        if (!syncLogin) return;

        wallpaperStatus->setText(wallpaper.name + " is applied. Approve the prompt to use it on the login screen too.");
        auto *process = new QProcess(this);
        connect(process, qOverload<int, QProcess::ExitStatus>(&QProcess::finished), this,
                [this, process, wallpaper](int code, QProcess::ExitStatus) {
            wallpaperStatus->setText(code == 0
                ? wallpaper.name + " is now the desktop, lock-screen, and login wallpaper."
                : "Desktop and lock screen changed, but login sync was cancelled or failed.");
            process->deleteLater();
        });
        process->start("/usr/bin/pkexec", {"/usr/libexec/proper-set-login-wallpaper", wallpaper.id});
    }

    QVector<AppearanceVariant> variants;
    QVector<Wallpaper> wallpapers;
    QVector<TextPreset> textPresets;
    QVector<QToolButton *> variantCards;
    QVector<QToolButton *> wallpaperCards;
    QGridLayout *variantGrid = nullptr;
    QButtonGroup *variantGroup = nullptr;
    QButtonGroup *textGroup = nullptr;
    QButtonGroup *wallpaperGroup = nullptr;
    QGridLayout *wallpaperGrid = nullptr;
    QLabel *variantStatus = nullptr;
    QLabel *wallpaperStatus = nullptr;
    int wallpaperColumns = 0;
    int variantColumns = 0;
};

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    QApplication::setOrganizationName("Proper Linux");
    QApplication::setApplicationName("Appearance");
    ProperAppearance window;
    window.show();
    return application.exec();
}
