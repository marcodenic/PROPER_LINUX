#include "proper-action-button.h"
#include "proper-material-window.h"
#include "proper-help.h"
#include <QApplication>
#include <QCloseEvent>
#include <QDBusConnection>
#include <QDBusMessage>
#include <QDesktopServices>
#include <QFile>
#include <QFontDatabase>
#include <QFrame>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QKeyEvent>
#include <QJsonDocument>
#include <QJsonObject>
#include <QLinearGradient>
#include <QList>
#include <QPainter>
#include <QPalette>
#include <QProcess>
#include <QPushButton>
#include <QResizeEvent>
#include <QScreen>
#include <QScrollArea>
#include <QTimer>
#include <QVBoxLayout>
#include <functional>
#include <initializer_list>

static void applyStyle(QApplication &application, const QString &path) {
    QFile style(path);
    if (style.open(QIODevice::ReadOnly | QIODevice::Text))
        application.setStyleSheet(QString::fromUtf8(style.readAll()));
}

static void applyProperWidgetStyle(QApplication &application) {
    const QString requested = qEnvironmentVariable("PROPER_UI_VARIANT").toLower();
    const bool light = requested == "light"
        || (requested != "dark" && application.palette().color(QPalette::Window).lightness() > 128);
    const QString root = qEnvironmentVariable("PROPER_UI_STYLE_DIR", "/usr/share/proper-linux/ui");
    applyStyle(application, root + QStringLiteral("/proper-widgets-")
               + (light ? QStringLiteral("light.qss") : QStringLiteral("dark.qss")));
}

static QIcon properIcon(const QString &name) {
    const QString root = qEnvironmentVariable("PROPER_ICON_DIR", "/usr/share/icons/hicolor/scalable/apps");
    return QIcon::fromTheme(name, QIcon(root + "/" + name + ".svg"));
}

static QColor semanticColour(const QString &group, const QString &name,
                             const QString &fallback) {
    static const QJsonObject palette = [] {
        const QString root = qEnvironmentVariable("PROPER_UI_STYLE_DIR", "/usr/share/proper-linux/ui");
        QFile file(root + "/proper-palette.json");
        if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
            return QJsonObject{};
        return QJsonDocument::fromJson(file.readAll()).object();
    }();
    const QColor colour(palette.value(group).toObject().value(name).toString());
    return colour.isValid() ? colour : QColor(fallback);
}

static QColor withAlpha(QColor colour, int alpha) {
    colour.setAlpha(alpha);
    return colour;
}

static QLabel *keycap(const QString &text) {
    auto *label = new QLabel(text);
    label->setObjectName("keycap");
    label->setAlignment(Qt::AlignCenter);
    label->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    return label;
}

static QWidget *shortcutHint(const QStringList &keys, const QString &action, bool compact = false) {
    auto *hint = new QFrame;
    hint->setObjectName(compact ? "shortcutLine" : "shortcutHint");
    auto *row = new QHBoxLayout(hint);
    row->setContentsMargins(compact ? 10 : 12, compact ? 8 : 9, compact ? 10 : 12, compact ? 8 : 9);
    row->setSpacing(6);
    for (int index = 0; index < keys.size(); ++index) {
        if (index > 0) {
            auto *plus = new QLabel("+");
            plus->setObjectName("keyJoin");
            row->addWidget(plus);
        }
        row->addWidget(keycap(keys[index]));
    }
    auto *copy = new QLabel(action);
    copy->setObjectName("shortcutAction");
    copy->setWordWrap(true);
    row->addWidget(copy, 1);
    return hint;
}

class IdleInhibitor final {
public:
    IdleInhibitor() {
        acquire("org.freedesktop.ScreenSaver", "/ScreenSaver",
                "org.freedesktop.ScreenSaver");
        acquire("org.freedesktop.PowerManagement",
                "/org/freedesktop/PowerManagement/Inhibit",
                "org.freedesktop.PowerManagement.Inhibit");
    }

    ~IdleInhibitor() {
        for (const Lease &lease : leases) {
            QDBusMessage release = QDBusMessage::createMethodCall(
                lease.service, lease.path, lease.interface, "UnInhibit");
            release << lease.cookie;
            QDBusConnection::sessionBus().call(release, QDBus::NoBlock);
        }
    }

private:
    struct Lease {
        QString service;
        QString path;
        QString interface;
        uint cookie;
    };

    QList<Lease> leases;

    void acquire(const QString &service, const QString &path,
                 const QString &interface) {
        QDBusMessage request = QDBusMessage::createMethodCall(
            service, path, interface, "Inhibit");
        request << QStringLiteral("Proper Welcome")
                << QStringLiteral("The live-session choice is open");
        const QDBusMessage reply = QDBusConnection::sessionBus().call(request);
        if (reply.type() == QDBusMessage::ReplyMessage &&
            !reply.arguments().isEmpty()) {
            leases.append({service, path, interface,
                           reply.arguments().constFirst().toUInt()});
        }
    }
};

class Wordmark final : public QWidget {
public:
    explicit Wordmark(QWidget *parent = nullptr) : QWidget(parent) {
        setAccessibleName("Proper");
        setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        setMinimumHeight(52);
    }

    QSize sizeHint() const override { return {426, 62}; }

protected:
    void paintEvent(QPaintEvent *) override {
        static const QStringList word = {"P", "R", "O", "P", "E", "R"};
        static const QHash<QString, QStringList> glyphs = {
            {"P", {"11110", "10001", "11110", "10000", "10000"}},
            {"R", {"11110", "10001", "11110", "10100", "10010"}},
            {"O", {"01110", "10001", "10001", "10001", "01110"}},
            {"E", {"11111", "10000", "11110", "10000", "11111"}},
        };

        constexpr qreal logicalWidth = 426.0;
        constexpr qreal logicalHeight = 62.0;
        const qreal scale = qMin(width() / logicalWidth, height() / logicalHeight);
        const qreal left = (width() - logicalWidth * scale) / 2.0;
        const qreal top = (height() - logicalHeight * scale) / 2.0;

        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);
        painter.translate(left, top);
        painter.scale(scale, scale);
        painter.setPen(Qt::NoPen);
        painter.setBrush(semanticColour("welcome", "wordmark", "#f7f8fa"));

        for (int letter = 0; letter < word.size(); ++letter) {
            const auto bitmap = glyphs.value(word.at(letter));
            const qreal offset = letter * 73.0;
            for (int row = 0; row < bitmap.size(); ++row) {
                for (int column = 0; column < bitmap.at(row).size(); ++column) {
                    if (bitmap.at(row).at(column) == QLatin1Char('1'))
                        painter.drawRoundedRect(QRectF(offset + column * 13.0, row * 13.0, 10.0, 10.0), .7, .7);
                }
            }
        }
    }
};

class Backdrop : public QWidget {
public:
    explicit Backdrop(QWidget *parent = nullptr) : QWidget(parent) {}

protected:
    void paintEvent(QPaintEvent *event) override {
        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);

        const QColor base = semanticColour("welcome", "base", "#050608");
        const QColor glow = semanticColour("welcome", "glow", "#1f3d62");
        const QColor glowMid = semanticColour("welcome", "glow_mid", "#0f2238");
        const QColor glowLow = semanticColour("welcome", "glow_low", "#0e233a");
        const QColor glowLowMid = semanticColour("welcome", "glow_low_mid", "#08121f");
        const QColor shadow = semanticColour("welcome", "shadow", "#000000");

        painter.fillRect(rect(), base);

        // Build depth from broad, soft pools of light instead of a visible
        // pattern. The centre remains calm behind the copy while the darker
        // perimeter keeps the full-screen live-session choice grounded.
        QRadialGradient upperGlow(QPointF(width() * .5, height() * .31), width() * .47);
        upperGlow.setColorAt(0.0, withAlpha(glow, 218));
        upperGlow.setColorAt(.42, withAlpha(glowMid, 166));
        upperGlow.setColorAt(1.0, withAlpha(base, 0));
        painter.fillRect(rect(), upperGlow);

        QRadialGradient lowerGlow(QPointF(width() * .5, height() * .68), width() * .68);
        lowerGlow.setColorAt(0.0, withAlpha(glowLow, 112));
        lowerGlow.setColorAt(.58, withAlpha(glowLowMid, 62));
        lowerGlow.setColorAt(1.0, withAlpha(base, 0));
        painter.fillRect(rect(), lowerGlow);

        QRadialGradient vignette(QPointF(width() * .5, height() * .48), width() * .74);
        vignette.setColorAt(0.0, withAlpha(shadow, 0));
        vignette.setColorAt(.62, withAlpha(shadow, 8));
        vignette.setColorAt(1.0, withAlpha(shadow, 178));
        painter.fillRect(rect(), vignette);

        QWidget::paintEvent(event);
    }
};

class Welcome final : public Backdrop {
public:
    Welcome() {
        setObjectName("properWelcome");
        setWindowTitle("Welcome to Proper Linux");
        setWindowIcon(properIcon("proper-logo-icon"));
        // Firmware and early live-session display negotiation can briefly
        // start at 640x480. Keep the choice usable there while KScreen moves
        // the QEMU review session to its preferred 1920x1080 mode.
        setMinimumSize(640, 480);
        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(38, 28, 38, 28);
        root->setSpacing(0);

        root->addStretch(2);

        auto *centre = new QWidget;
        // Keep the approved single-line headline composition. The action row
        // remains usable inside the transient 640px firmware fallback even
        // when the centred visual block extends slightly beyond its margins.
        centre->setMinimumWidth(680);
        centre->setMaximumWidth(820);
        auto *content = new QVBoxLayout(centre);
        content->setContentsMargins(0, 0, 0, 0);
        content->setSpacing(14);

        auto *mark = new Wordmark;
        mark->setMaximumWidth(520);
        mark->setMinimumHeight(76);
        content->addWidget(mark, 0, Qt::AlignHCenter);

        auto *linuxLabel = new QLabel("L I N U X");
        linuxLabel->setObjectName("eyebrow");
        linuxLabel->setAlignment(Qt::AlignCenter);
        content->addWidget(linuxLabel);
        content->addSpacing(15);

        auto *headline = new QLabel("Linux, considered.");
        headline->setObjectName("headline");
        headline->setAlignment(Qt::AlignCenter);
        headline->setWordWrap(true);
        headline->setMinimumHeight(56);
        content->addWidget(headline);

        auto *body = new QLabel(
            "Fedora’s solid foundation. KDE, carefully curated.\n"
            "A calmer desktop with thoughtful defaults — and nothing in your way."
        );
        body->setObjectName("body");
        body->setAlignment(Qt::AlignCenter);
        body->setWordWrap(true);
        body->setMinimumHeight(52);
        body->setMinimumWidth(680);
        body->setMaximumWidth(760);
        content->addWidget(body, 0, Qt::AlignHCenter);

        content->addSpacing(10);

        auto *actions = new QHBoxLayout;
        actions->setSpacing(16);
        actions->addStretch();
        auto *tryButton = new QPushButton("Try Proper");
        tryButton->setAccessibleName("Try Proper Linux without installing");
        tryButton->setMinimumWidth(276);
        auto *installButton = new QPushButton("Install Proper");
        installButton->setObjectName("primary");
        installButton->setAccessibleName("Install Proper Linux");
        installButton->setMinimumWidth(276);
        actions->addWidget(tryButton);
        actions->addWidget(installButton);
        actions->addStretch();
        content->addLayout(actions);
        installButton->setFocus();

        content->addSpacing(12);

        auto *shortcuts = new QHBoxLayout;
        shortcuts->setSpacing(4);
        shortcuts->addStretch();
        shortcuts->addWidget(shortcutHint({"Meta"}, "Search", true));
        shortcuts->addSpacing(20);
        shortcuts->addWidget(shortcutHint({"Meta", "W"}, "Arrange", true));
        shortcuts->addSpacing(20);
        shortcuts->addWidget(shortcutHint({"Meta", "Enter"}, "Terminal", true));
        shortcuts->addStretch();
        content->addLayout(shortcuts);

        root->addWidget(centre, 0, Qt::AlignHCenter);
        root->addStretch(3);

        connect(tryButton, &QPushButton::clicked, this, &QWidget::close);
        connect(installButton, &QPushButton::clicked, this, [this] {
            if (QProcess::startDetached("/usr/bin/liveinst", {}))
                this->close();
        });
    }
};

class Guide final : public ProperMaterialWindow {
public:
    Guide() {
        setObjectName("properRoot");
        setWindowTitle("Start Here · Proper Linux");
        setWindowIcon(properIcon("proper-logo-icon"));
        resize(980, 640);
        setMinimumSize(620, 460);

        auto *root = new QHBoxLayout(this);
        root->setSpacing(0);
        root->setContentsMargins(0, 0, 0, 0);

        auto *scroll = new QScrollArea;
        scroll->setWidgetResizable(true);
        scroll->setFrameShape(QFrame::NoFrame);
        scroll->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        auto *content = new QWidget;
        auto *page = new QVBoxLayout(content);
        page->setContentsMargins(34, 30, 34, 26);
        page->setSpacing(12);

        auto *hero = new QFrame;
        hero->setObjectName("guideGreeting");
        auto *header = new QVBoxLayout(hero);
        hero->setFixedWidth(280);
        header->setContentsMargins(26, 36, 26, 24);
        header->setSpacing(16);
        auto *mark = new QLabel;
        mark->setPixmap(properIcon("proper-logo-icon").pixmap(58, 58));
        mark->setFixedSize(64, 64);
        header->addWidget(mark, 0, Qt::AlignTop);
        auto *copy = new QVBoxLayout;
        copy->setSpacing(6);
        auto *eyebrow = new QLabel("WELCOME TO PROPER");
        eyebrow->setObjectName("guideEyebrow");
        copy->addWidget(eyebrow);
        auto *title = new QLabel("Make yourself at home.");
        QFont titleFont = title->font();
        titleFont.setPointSizeF(titleFont.pointSizeF() * 2.1);
        titleFont.setBold(true);
        title->setFont(titleFont);
        title->setWordWrap(true);
        copy->addWidget(title);
        auto *intro = new QLabel(
            "Your browser, terminal, and file manager are ready. "
            "Add your favourite apps, choose a wallpaper, and get on with your day."
        );
        intro->setObjectName("guideCopy");
        intro->setWordWrap(true);
        copy->addWidget(intro);
        header->addLayout(copy);
        header->addStretch();
        header->addWidget(materialControl(hero));
        root->addWidget(hero);
        setNavigation(hero);

        status = new QLabel;
        status->setObjectName("errorBanner");
        status->setWordWrap(true);
        status->hide();
        page->addWidget(status);

        auto *section = new QLabel("Make it yours");
        section->setObjectName("guideSectionLabel");
        page->addWidget(section);

        actionGrid = new QGridLayout;
        actionGrid->setHorizontalSpacing(12);
        actionGrid->setVerticalSpacing(12);
        actionCards = {
            makeCard("Find your apps", "A few favourites, and more when you need them.",
                     "proper-apps", [this] { launch("Proper Apps", "/usr/bin/proper-apps"); }, true),
            makeCard("Choose your look", "Desktop styles, text sizes and wallpapers.",
                     "proper-appearance", [this] { launch("Appearance", "/usr/bin/proper-appearance"); }, true)
        };
        page->addLayout(actionGrid);
        auto *everyday = new QLabel("Everyday essentials");
        everyday->setObjectName("guideSectionLabel");
        page->addWidget(everyday);
        page->addWidget(makeCard("System Settings", "Displays, sound, network and connected devices.",
            "systemsettings", [this] { launch("System Settings", "/usr/bin/systemsettings"); }));
        page->addWidget(makeCard("Check for updates", "Keep Fedora and your applications up to date.",
            "system-software-update", [this] { launch("Updates", "/usr/bin/proper-tool", {"updates"}); }));
        page->addWidget(makeCard("Keyboard shortcuts", "Useful shortcuts, with pointer routes for every action.",
            "proper-shortcuts", [this] { launch("Keyboard shortcuts", "/usr/bin/proper-welcome", {"--shortcuts"}); }));
        page->addWidget(makeCard("Help & feedback", "Everyday guidance, available offline.",
            "help-contents", [this] { openHelp(); }));
        page->addStretch();

        auto *footer = new QLabel("Proper Linux · Built on Fedora and KDE");
        footer->setObjectName("guideFooter");
        footer->setAlignment(Qt::AlignCenter);
        footer->setWordWrap(true);
        page->addWidget(footer);
        scroll->setWidget(content);
        root->addWidget(scroll, 1);
        rebuildGrid(width() - 280);
    }

protected:
    void resizeEvent(QResizeEvent *event) override {
        ProperMaterialWindow::resizeEvent(event);
        rebuildGrid(event->size().width() - 280);
    }

private:
    QWidget *makeCard(const QString &title, const QString &description, const QString &icon,
                      std::function<void()> action, bool primary = false) {
        auto *card = new ProperActionButton;
        card->setObjectName(primary ? "guideAction" : "guideLink");
        card->setAccessibleName(title);
        card->setAccessibleDescription(description);
        card->setCursor(Qt::PointingHandCursor);
        card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
        auto *row = new QHBoxLayout(card);
        const int verticalInset = primary ? 18 : 8;
        row->setContentsMargins(18, verticalInset, 18, verticalInset);
        row->setSpacing(16);
        auto *art = new QLabel;
        art->setPixmap(properIcon(icon).pixmap(28, 28));
        art->setFixedSize(32, 32);
        row->addWidget(art);
        auto *copy = new QVBoxLayout;
        copy->setSpacing(5);
        auto *heading = new QLabel(title);
        heading->setObjectName("guideCardTitle");
        heading->setWordWrap(true);
        copy->addWidget(heading);
        auto *body = new QLabel(description);
        body->setObjectName("guideCopy");
        body->setWordWrap(true);
        copy->addWidget(body);
        row->addLayout(copy, 1);
        auto *arrow = new QLabel;
        arrow->setPixmap(QIcon::fromTheme("go-next").pixmap(16, 16));
        row->addWidget(arrow);
        for (auto *label : card->findChildren<QLabel *>())
            label->setAttribute(Qt::WA_TransparentForMouseEvents);
        connect(card, &QPushButton::clicked, this, [action = std::move(action)] { action(); });
        return card;
    }

    void rebuildGrid(int width) {
        const int wanted = width >= 700 ? 2 : 1;
        if (wanted == actionColumns && actionGrid->count() == actionCards.size())
            return;
        actionColumns = wanted;
        while (auto *item = actionGrid->takeAt(0)) delete item;
        for (int index = 0; index < actionCards.size(); ++index)
            actionGrid->addWidget(actionCards[index], index / actionColumns, index % actionColumns);
        for (int column = 0; column < actionColumns; ++column)
            actionGrid->setColumnStretch(column, 1);
    }

    void launch(const QString &name, const QString &program, const QStringList &arguments = {}) {
        status->hide();
        if (!QProcess::startDetached(program, arguments))
            showFailure(name + " could not start. Try again, or use Help & feedback. Details: " + program);
    }

    void openHelp() {
        auto *help = new ProperHelp(this);
        help->show();
    }

    void showFailure(const QString &message) {
        status->setText(message);
        status->show();
    }

    QLabel *status = nullptr;
    QGridLayout *actionGrid = nullptr;
    QVector<QWidget *> actionCards;
    int actionColumns = 0;
};

class ShortcutOverview final : public QWidget {
public:
    ShortcutOverview() {
        setObjectName("properRoot");
        setWindowTitle("Keyboard shortcuts · Proper Linux");
        setWindowIcon(properIcon("proper-shortcuts"));
        resize(900, 640);
        setMinimumSize(620, 460);

        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(26, 24, 26, 22);
        root->setSpacing(14);
        auto *eyebrow = new QLabel("QUICK REFERENCE");
        eyebrow->setObjectName("guideEyebrow");
        root->addWidget(eyebrow);
        auto *title = new QLabel("Keyboard shortcuts");
        QFont titleFont = title->font();
        titleFont.setPointSizeF(titleFont.pointSizeF() * 1.8);
        titleFont.setBold(true);
        title->setFont(titleFont);
        root->addWidget(title);
        auto *intro = new QLabel("Meta is the Windows or Super key. Use the shelf for apps and Command Centre, and window menus for arrangement. Press Esc to close.");
        intro->setObjectName("guideCopy");
        intro->setWordWrap(true);
        root->addWidget(intro);

        auto *scroll = new QScrollArea;
        scroll->setWidgetResizable(true);
        scroll->setFrameShape(QFrame::NoFrame);
        auto *content = new QWidget;
        auto *grid = new QGridLayout(content);
        grid->setContentsMargins(0, 6, 8, 6);
        grid->setHorizontalSpacing(14);
        grid->setVerticalSpacing(14);
        grid->addWidget(section("Launch", {
            {{"Meta"}, "Search apps, files, and actions"},
            {{"Meta", "Enter"}, "Open Ghostty"},
            {{"Meta", "/"}, "Show this shortcut pane"}
        }), 0, 0);
        grid->addWidget(section("Windows", {
            {{"Meta", "← / →"}, "Tile to a half"},
            {{"Meta", "1 / 3 / 7 / 9"}, "Tile to a quadrant"},
            {{"Meta", "W"}, "Arrange or restore the workspace"},
            {{"Meta", "↑ / ↓"}, "Maximise or restore"},
            {{"Meta", "H"}, "Minimise"}
        }), 0, 1);
        grid->addWidget(section("Workspace", {
            {{"Meta", "O"}, "Overview"},
            {{"Meta", "S"}, "Command Centre"},
            {{"Meta", "G"}, "Desktop grid"},
            {{"Meta", "D"}, "Peek at the desktop"},
            {{"Meta", "T"}, "Edit tiling layout"}
        }), 1, 0);
        grid->addWidget(section("Capture", {
            {{"Print"}, "Open Spectacle"},
            {{"Meta", "Shift", "S"}, "Capture a region"},
            {{"Meta", "Shift", "O"}, "Copy text from a region"},
            {{"Meta", "V"}, "Clipboard history"}
        }), 1, 1);
        grid->setColumnStretch(0, 1);
        grid->setColumnStretch(1, 1);
        scroll->setWidget(content);
        root->addWidget(scroll, 1);

        auto *actions = new QHBoxLayout;
        auto *full = new QPushButton("Open searchable reference");
        auto *close = new QPushButton("Close");
        close->setObjectName("primaryButton");
        actions->addWidget(full);
        actions->addStretch();
        actions->addWidget(close);
        root->addLayout(actions);
        connect(full, &QPushButton::clicked, this, [] {
            QDesktopServices::openUrl(QUrl("file:///usr/share/doc/proper-launchers/proper-shortcuts.html"));
        });
        connect(close, &QPushButton::clicked, this, &QWidget::close);
    }

protected:
    void keyPressEvent(QKeyEvent *event) override {
        if (event->key() == Qt::Key_Escape) {
            close();
            return;
        }
        QWidget::keyPressEvent(event);
    }

private:
    using Shortcut = QPair<QStringList, QString>;

    static QWidget *section(const QString &name, std::initializer_list<Shortcut> shortcuts) {
        auto *panel = new QFrame;
        panel->setObjectName("shortcutPanel");
        auto *layout = new QVBoxLayout(panel);
        layout->setContentsMargins(14, 13, 14, 14);
        layout->setSpacing(7);
        auto *title = new QLabel(name.toUpper());
        title->setObjectName("guideSectionLabel");
        layout->addWidget(title);
        for (const auto &item : shortcuts)
            layout->addWidget(shortcutHint(item.first, item.second, true));
        layout->addStretch();
        return panel;
    }
};

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    if (QIcon::themeName().isEmpty())
        QIcon::setThemeName("breeze");
    QApplication::setApplicationName("Proper Welcome");
    QApplication::setDesktopFileName("org.properlinux.Welcome");

    const int screenshotOption = application.arguments().indexOf("--screenshot");
    if (application.arguments().contains("--shortcuts")) {
        QApplication::setApplicationName("Proper Shortcuts");
        QApplication::setDesktopFileName("proper-shortcut-overview");
        applyProperWidgetStyle(application);
        ShortcutOverview overview;
        overview.show();
        if (screenshotOption >= 0 && screenshotOption + 1 < application.arguments().size()) {
            const QString output = application.arguments().at(screenshotOption + 1);
            QTimer::singleShot(250, &overview, [&application, &overview, output] {
                application.exit(overview.grab().save(output) ? 0 : 2);
            });
        }
        return application.exec();
    }
    if (application.arguments().contains("--guide")) {
        QApplication::setApplicationName("Start Here");
        QApplication::setDesktopFileName("proper-start");
        applyProperWidgetStyle(application);
        Guide guide;
        guide.show();
        if (screenshotOption >= 0 && screenshotOption + 1 < application.arguments().size()) {
            const QString output = application.arguments().at(screenshotOption + 1);
            QTimer::singleShot(250, &guide, [&application, &guide, output] {
                application.exit(guide.grab().save(output) ? 0 : 2);
            });
        }
        return application.exec();
    }

    if (application.arguments().contains("--install"))
        return QProcess::startDetached("/usr/bin/liveinst", {}) ? 0 : 1;

    const QString styleRoot = qEnvironmentVariable("PROPER_UI_STYLE_DIR", "/usr/share/proper-linux/ui");
    applyStyle(application, styleRoot + "/proper-welcome.qss");
    IdleInhibitor idleInhibitor;
    Welcome window;
    if (application.arguments().contains("--windowed") || screenshotOption >= 0) {
        window.resize(1120, 680);
        window.show();
    } else {
        window.setWindowFlag(Qt::FramelessWindowHint);
        window.showMaximized();
    }
    if (screenshotOption >= 0 && screenshotOption + 1 < application.arguments().size()) {
        const QString output = application.arguments().at(screenshotOption + 1);
        QTimer::singleShot(250, &window, [&application, &window, output] {
            application.exit(window.grab().save(output) ? 0 : 2);
        });
    }
    return application.exec();
}
