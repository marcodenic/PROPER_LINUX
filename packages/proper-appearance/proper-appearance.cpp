#include "proper-material-window.h"
#include <QApplication>
#include <QStackedWidget>
#include <QButtonGroup>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QIcon>
#include <QJsonDocument>
#include <QJsonObject>
#include <QLabel>
#include <QPainter>
#include <QPalette>
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
    QString colorScheme;
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

static void applyProperWidgetStyle(QApplication &application, const QString &explicitVariant = {}) {
    const QString requested = explicitVariant.isEmpty()
        ? qEnvironmentVariable("PROPER_UI_VARIANT").toLower()
        : explicitVariant.toLower();
    const bool light = requested == "light"
        || (requested != "dark" && application.palette().color(QPalette::Window).lightness() > 128);
    const QString root = qEnvironmentVariable("PROPER_UI_STYLE_DIR", "/usr/share/proper-linux/ui");
    QFile style(root + QStringLiteral("/proper-widgets-")
                + (light ? QStringLiteral("light.qss") : QStringLiteral("dark.qss")));
    if (style.open(QIODevice::ReadOnly | QIODevice::Text))
        application.setStyleSheet(QString::fromUtf8(style.readAll()));
}

static QIcon properIcon(const QString &name) {
    const QString root = qEnvironmentVariable("PROPER_ICON_DIR", "/usr/share/icons/hicolor/scalable/apps");
    return QIcon::fromTheme(name, QIcon(root + "/" + name + ".svg"));
}

static QJsonObject properPalette() {
    const QString root = qEnvironmentVariable("PROPER_UI_STYLE_DIR", "/usr/share/proper-linux/ui");
    QFile file(root + "/proper-palette.json");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return {};
    return QJsonDocument::fromJson(file.readAll()).object();
}

static QColor semanticColour(const QJsonObject &palette, const QString &variant,
                             const QString &name, const QString &fallback) {
    const QColor colour(palette.value("colour").toObject()
                            .value(variant).toObject()
                            .value(name).toString());
    return colour.isValid() ? colour : QColor(fallback);
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

class ProperAppearance final : public ProperMaterialWindow {
public:
    ProperAppearance() {
        setObjectName("properRoot");
        setWindowTitle("Appearance");
        setWindowIcon(properIcon("proper-appearance"));
        resize(1120, 640);
        setMinimumSize(760, 520);

        const QJsonObject palette = properPalette();
        variants = {
            {"com.properlinux.dark.desktop", "Proper", "Blue Hour", "Balanced dark · Proper default", "ProperBlueHour",
             "/usr/share/wallpapers/ProperBlueHour/contents/images/1920x1080.png",
             semanticColour(palette, "dark", "base", "#11151d"),
             semanticColour(palette, "dark", "surface", "#181d25"),
             semanticColour(palette, "dark", "text", "#f1f4f8"),
             semanticColour(palette, "dark", "accent", "#91b4ff")},
            {"com.properlinux.light.desktop", "ProperLight", "Alpine Light", "Light surfaces · frosted shelf", "ProperHorizon",
             "/usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png",
             semanticColour(palette, "light", "base", "#f6f7fb"),
             semanticColour(palette, "light", "surface", "#ffffff"),
             semanticColour(palette, "light", "text", "#18202b"),
             semanticColour(palette, "light", "accent", "#3b68d9")},
            {"com.properlinux.midnight.desktop", "ProperMidnight", "Midnight", "Deeper contrast · cool blue focus", "summer_1am",
             "/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg",
             semanticColour(palette, "midnight", "base", "#090d14"),
             semanticColour(palette, "midnight", "surface", "#0c1119"),
             semanticColour(palette, "midnight", "text", "#f5f7fa"),
             semanticColour(palette, "midnight", "accent", "#79a8ff")},
        };
        wallpapers = {
            {"ProperBlueHour", "Proper Blue Hour", "/usr/share/wallpapers/ProperBlueHour/contents/images/1920x1080.png"},
            {"ProperHorizon", "Alpine Morning", "/usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png"},
            {"Path", "Path", "/usr/share/wallpapers/Path/contents/images/2560x1600.jpg"},
            {"Volna", "Volna", "/usr/share/wallpapers/Volna/contents/images/5120x2880.jpg"},
            {"summer_1am", "Summer 1 AM", "/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg"},
            {"ProperRallyBlueHour", "Rally: Blue Hour", "/usr/share/wallpapers/ProperRallyBlueHour/contents/images/1920x1080.png"},
            {"ProperRallyNightFlight", "Rally: Night Flight", "/usr/share/wallpapers/ProperRallyNightFlight/contents/images/1920x1080.png"},
            {"ProperFloatingFalls", "Floating Falls", "/usr/share/wallpapers/ProperFloatingFalls/contents/images/1920x1080.png"},
            {"ProperTerracedDawn", "Terraced Dawn", "/usr/share/wallpapers/ProperTerracedDawn/contents/images/1920x1080.png"},
            {"ProperGlacialArch", "Glacial Arch", "/usr/share/wallpapers/ProperGlacialArch/contents/images/1920x1080.png"},
            {"ProperHighlandBlueHour", "Highland Blue Hour", "/usr/share/wallpapers/ProperHighlandBlueHour/contents/images/1920x1080.png"},
            {"ProperHighlandSunrise", "Highland Sunrise", "/usr/share/wallpapers/ProperHighlandSunrise/contents/images/1920x1080.png"},
            {"ProperSaltFlatStation", "Salt-Flat Station", "/usr/share/wallpapers/ProperSaltFlatStation/contents/images/1920x1080.png"},
        };
        textPresets = {
            {"compact", "Compact", "More room", 9, 8, 11},
            {"standard", "Standard", "Proper default", 10, 9, 12},
            {"large", "Large", "Easier to read", 12, 10, 14},
        };

        buildNavigation();

        auto stylePage = makePage("Desktop style", "Preview a coordinated look, then apply it when you are ready.");
        auto *root = stylePage.body;
        variantGroup = new QButtonGroup(this);
        variantGroup->setExclusive(true);
        variantGrid = new QGridLayout;
        variantGrid->setSpacing(16);
        variantGrid->setAlignment(Qt::AlignLeft | Qt::AlignTop);
        for (int index = 0; index < variants.size(); ++index) {
            const auto &variant = variants[index];
            auto *card = new QToolButton;
            card->setText(variant.name + "\n" + variant.description);
            card->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
            card->setCheckable(true);
            card->setFocusPolicy(Qt::StrongFocus);
            card->setMinimumSize(220, 192);
            card->setMaximumWidth(260);
            card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            card->setIcon(QIcon(variantPreview(variant)));
            card->setIconSize(QSize(240, 124));
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
        stylePage.footer->addLayout(variantActions);
        root->addStretch();

        auto textPage = makePage("Text size", "Choose the size that feels comfortable across your desktop and apps.");
        root = textPage.body;
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
            button->setFocusPolicy(Qt::StrongFocus);
            button->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            textGroup->addButton(button, index);
            textRow->addWidget(button);
        }
        auto *applyTextButton = new QPushButton("Use text size");
        root->addLayout(textRow);
        textPreview = new QLabel("Make yourself at home.\n\nYour files, favourite apps and everyday work, at a size that is comfortable to read.");
        textPreview->setWordWrap(true);
        textPreview->setMargin(24);
        root->addWidget(textPreview);
        root->addStretch();
        textPage.footer->addWidget(applyTextButton, 0, Qt::AlignRight);

        auto wallpaperPage = makePage("Wallpapers", "Choose a background for your desktop and lock screen.");
        root = wallpaperPage.body;
        wallpaperGroup = new QButtonGroup(this);
        wallpaperGroup->setExclusive(true);
        wallpaperGrid = new QGridLayout;
        wallpaperGrid->setAlignment(Qt::AlignLeft | Qt::AlignTop);
        wallpaperGrid->setHorizontalSpacing(18);
        wallpaperGrid->setVerticalSpacing(18);
        for (int index = 0; index < wallpapers.size(); ++index) {
            const auto &wallpaper = wallpapers[index];
            auto *card = new QToolButton;
            card->setText(wallpaper.name);
            card->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
            card->setCheckable(true);
            card->setFocusPolicy(Qt::StrongFocus);
            card->setMinimumSize(210, 156);
            card->setMaximumWidth(244);
            card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            card->setIconSize(QSize(224, 126));
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
        wallpaperPage.footer->addLayout(wallpaperActions);
        root->addStretch();


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
        updateTextPreview(textIndex);
        connect(textGroup, &QButtonGroup::idClicked, this, [this](int index) { updateTextPreview(index); });
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
        ProperMaterialWindow::resizeEvent(event);
        rebuildVariantGrid(event->size().width());
        rebuildWallpaperGrid(event->size().width());
    }

private:
    void buildNavigation() {
        auto *outer = new QHBoxLayout(this);
        outer->setContentsMargins(0, 0, 0, 0);
        outer->setSpacing(0);
        auto *navigation = new QWidget;
        navigation->setFixedWidth(210);
        auto *nav = new QVBoxLayout(navigation);
        nav->setContentsMargins(18, 24, 18, 20);
        auto *brand = new QLabel("Appearance");
        QFont brandFont = brand->font();
        brandFont.setBold(true);
        brand->setFont(brandFont);
        nav->addWidget(brand);
        nav->addSpacing(14);
        pages = new QStackedWidget;
        auto *sections = new QButtonGroup(this);
        const QStringList names = {"Desktop style", "Text size", "Wallpapers"};
        for (int index = 0; index < names.size(); ++index) {
            auto *button = new QToolButton;
            button->setText(names[index]);
            button->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            button->setCheckable(true);
            button->setFocusPolicy(Qt::StrongFocus);
            button->setObjectName("navButton");
            button->setMinimumHeight(36);
            sections->addButton(button, index);
            nav->addWidget(button);
        }
        sections->button(0)->setChecked(true);
        connect(sections, &QButtonGroup::idClicked, pages, &QStackedWidget::setCurrentIndex);
        nav->addStretch();
        nav->addWidget(materialControl(navigation));
        setNavigation(navigation);
        outer->addWidget(navigation);
        outer->addWidget(pages, 1);

    }

    void updateTextPreview(int index) {
        QFont font = textPreview->font();
        font.setPointSize(textPresets[index].uiSize);
        textPreview->setFont(font);
    }

    struct AppearancePage { QVBoxLayout *body; QVBoxLayout *footer; };

    AppearancePage makePage(const QString &title, const QString &description) {
        auto *page = new QWidget;
        auto *layout = new QVBoxLayout(page);
        layout->setContentsMargins(26, 24, 26, 20);
        layout->setSpacing(16);
        auto *heading = new QLabel(title);
        QFont font = heading->font();
        font.setPointSizeF(font.pointSizeF() * 1.8);
        font.setBold(true);
        heading->setFont(font);
        layout->addWidget(heading);
        auto *copy = new QLabel(description);
        copy->setObjectName("subtitle");
        copy->setWordWrap(true);
        layout->addWidget(copy);
        auto *scroll = new QScrollArea;
        scroll->setWidgetResizable(true);
        scroll->setFrameShape(QFrame::NoFrame);
        auto *content = new QWidget;
        auto *body = new QVBoxLayout(content);
        body->setContentsMargins(0, 0, 0, 0);
        body->setSpacing(12);
        scroll->setWidget(content);
        layout->addWidget(scroll, 1);
        auto *footer = new QVBoxLayout;
        layout->addLayout(footer);
        pages->addWidget(page);
        return {body, footer};
    }

    void rebuildWallpaperGrid(int width) {
        const int wanted = qMax(1, (width - 244) / 254);
        if (wanted == wallpaperColumns && wallpaperGrid->count() == wallpaperCards.size()) return;
        wallpaperColumns = wanted;
        while (auto *item = wallpaperGrid->takeAt(0)) delete item;
        for (int index = 0; index < wallpaperCards.size(); ++index)
            wallpaperGrid->addWidget(wallpaperCards[index], index / wallpaperColumns, index % wallpaperColumns);
    }

    void rebuildVariantGrid(int width) {
        const int wanted = width >= 1040 ? 3 : width >= 760 ? 2 : 1;
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
        const QString colorTool = QStandardPaths::findExecutable("plasma-apply-colorscheme");
        if (colorTool.isEmpty() || QProcess::execute(colorTool, {variant.colorScheme}) != 0) {
            variantStatus->setText("The desktop layout changed, but its complete colour palette could not be applied. Reinstall Proper Appearance and retry.");
            return;
        }
        if (QFileInfo::exists(variant.wallpaperPath))
            QProcess::execute("/usr/bin/plasma-apply-wallpaperimage", {variant.wallpaperPath});
        applyProperWidgetStyle(*qApp, variant.id == "com.properlinux.light.desktop" ? "light" : "dark");
        QSettings preferences(configRoot() + "/proper-linux/appearance.ini", QSettings::IniFormat);
        preferences.setValue("Appearance/variant", variant.id);
        variantStatus->setText(variant.name + " is now active. Open apps keep their current palette until restarted.");
    }

    static bool runConfigWrite(const QString &group, const QString &key, const QString &value) {
        const QString tool = QStandardPaths::findExecutable("kwriteconfig6");
        return !tool.isEmpty() && QProcess::execute(tool, {"--notify", "--file", "kdeglobals", "--group", group, "--key", key, value}) == 0;
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
        settings.setValue("gtk-font-name", QString("Inter %1").arg(size));
        settings.endGroup();
        settings.sync();
    }

    void applyTextPreset() {
        const int index = textGroup->checkedId();
        if (index < 0 || index >= textPresets.size()) return;
        const auto &preset = textPresets[index];
        const QString normal = QString("Inter,%1,-1,5,50,0,0,0,0,0").arg(preset.uiSize);
        const QString toolbar = QString("Inter,%1,-1,5,50,0,0,0,0,0").arg(qMax(8, preset.uiSize - 1));
        const QString small = QString("Inter,%1,-1,5,50,0,0,0,0,0").arg(preset.smallSize);
        const QString title = QString("Inter,%1,-1,5,50,0,0,0,0,0").arg(qMax(8, preset.uiSize - 1));
        bool ok = true;
        for (const QString &key : {QString("desktopFont"), QString("font"), QString("menuFont")})
            ok = runConfigWrite("General", key, normal) && ok;
        ok = runConfigWrite("General", "toolBarFont", toolbar) && ok;
        ok = runConfigWrite("General", "smallestReadableFont", small) && ok;
        ok = runConfigWrite("WM", "activeFont", title) && ok;
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
            QProcess::execute(qdbus, {"org.kde.KGlobalSettings", "/KGlobalSettings", "org.kde.KGlobalSettings.notifyChange", "0", "0"});
        QFont applicationFont("Inter");
        applicationFont.setPointSize(preset.uiSize);
        qApp->setFont(applicationFont);
        variantStatus->setText(preset.name + " text is active. The desktop and this window update now; some already-open apps may need to be reopened.");
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
    QLabel *textPreview = nullptr;
    QStackedWidget *pages = nullptr;
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
    if (QIcon::themeName().isEmpty())
        QIcon::setThemeName("breeze");
    QApplication::setOrganizationName("Proper Linux");
    QApplication::setApplicationName("Appearance");
    QApplication::setDesktopFileName("proper-appearance");
    applyProperWidgetStyle(application);
    ProperAppearance window;
    window.show();
    return application.exec();
}
