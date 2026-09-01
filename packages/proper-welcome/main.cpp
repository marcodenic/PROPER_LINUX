#include <QApplication>
#include <QCloseEvent>
#include <QDBusConnection>
#include <QDBusMessage>
#include <QDesktopServices>
#include <QFile>
#include <QFontDatabase>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QLinearGradient>
#include <QList>
#include <QPainter>
#include <QPalette>
#include <QProcess>
#include <QPushButton>
#include <QScreen>
#include <QTimer>
#include <QVBoxLayout>
#include <functional>

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
        painter.setBrush(QColor("#f7f8fa"));

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

        QRadialGradient glow(QPointF(width() * .5, height() * .42), width() * .48);
        glow.setColorAt(0.0, QColor(24, 46, 73, 210));
        glow.setColorAt(.48, QColor(9, 15, 24, 235));
        glow.setColorAt(1.0, QColor("#050608"));
        painter.fillRect(rect(), glow);

        painter.setPen(QPen(QColor(160, 192, 225, 9), 1));
        constexpr int step = 40;
        for (int x = step; x < width(); x += step)
            painter.drawLine(x, 0, x, height());
        for (int y = step; y < height(); y += step)
            painter.drawLine(0, y, width(), y);

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

        auto *top = new QHBoxLayout;
        auto *live = new QLabel("LIVE SESSION");
        live->setObjectName("liveBadge");
        top->addWidget(live);
        top->addStretch();
        auto *closeButton = new QPushButton("×");
        closeButton->setObjectName("close");
        closeButton->setAccessibleName("Close welcome and try Proper Linux");
        top->addWidget(closeButton);
        root->addLayout(top);
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

        auto *headline = new QLabel("A considered desktop, ready to explore.");
        headline->setObjectName("headline");
        headline->setAlignment(Qt::AlignCenter);
        headline->setWordWrap(true);
        headline->setMinimumHeight(56);
        content->addWidget(headline);

        auto *body = new QLabel("Try the complete desktop without changing this computer, or install Proper Linux when you’re ready.");
        body->setObjectName("body");
        body->setAlignment(Qt::AlignCenter);
        body->setWordWrap(true);
        body->setMinimumHeight(58);
        body->setMaximumWidth(650);
        content->addWidget(body, 0, Qt::AlignHCenter);
        content->addSpacing(17);

        auto *actions = new QHBoxLayout;
        actions->setSpacing(12);
        actions->addStretch();
        auto *tryButton = new QPushButton("Try Proper");
        tryButton->setAccessibleName("Try Proper Linux without installing");
        auto *installButton = new QPushButton("Install Proper");
        installButton->setObjectName("primary");
        installButton->setAccessibleName("Install Proper Linux");
        actions->addWidget(tryButton);
        actions->addWidget(installButton);
        actions->addStretch();
        content->addLayout(actions);

        root->addWidget(centre, 0, Qt::AlignHCenter);
        root->addStretch(3);

        auto *footer = new QLabel("Proper Linux 0.1");
        footer->setObjectName("footer");
        footer->setAlignment(Qt::AlignCenter);
        root->addWidget(footer);

        connect(closeButton, &QPushButton::clicked, this, &QWidget::close);
        connect(tryButton, &QPushButton::clicked, this, &QWidget::close);
        connect(installButton, &QPushButton::clicked, this, [this] {
            if (QProcess::startDetached("/usr/bin/liveinst", {}))
                this->close();
        });
    }
};

class Guide final : public QWidget {
public:
    Guide() {
        setObjectName("properRoot");
        setWindowTitle("Start Here · Proper Linux");
        setWindowIcon(properIcon("proper-logo-icon"));
        resize(900, 640);
        setMinimumSize(680, 500);

        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(34, 30, 34, 26);
        root->setSpacing(20);

        auto *header = new QHBoxLayout;
        auto *mark = new QLabel;
        mark->setPixmap(properIcon("proper-logo-icon").pixmap(58, 58));
        mark->setFixedSize(64, 64);
        header->addWidget(mark, 0, Qt::AlignTop);
        auto *copy = new QVBoxLayout;
        auto *title = new QLabel("Start here");
        QFont titleFont = title->font();
        titleFont.setPixelSize(30);
        titleFont.setBold(true);
        title->setFont(titleFont);
        copy->addWidget(title);
        auto *intro = new QLabel("The useful parts of Proper Linux, gathered in one quiet place.");
        intro->setObjectName("guideCopy");
        intro->setWordWrap(true);
        copy->addWidget(intro);
        header->addLayout(copy, 1);
        root->addLayout(header);

        status = new QLabel;
        status->setObjectName("errorBanner");
        status->setWordWrap(true);
        status->hide();
        root->addWidget(status);

        auto *grid = new QGridLayout;
        grid->setHorizontalSpacing(14);
        grid->setVerticalSpacing(14);
        addCard(grid, 0, 0, "Browse software", "Recommended apps and the full catalogue",
                "proper-apps", [this] { launch("/usr/bin/proper-apps"); });
        addCard(grid, 0, 1, "Change appearance", "Desktop styles, text size, and wallpapers",
                "proper-appearance", [this] { launch("/usr/bin/proper-appearance"); });
        addCard(grid, 1, 0, "Check for updates", "System and application updates in Discover",
                "system-software-update", [this] { launch("/usr/bin/proper-tool", {"updates"}); });
        addCard(grid, 1, 1, "Learn shortcuts", "Fast paths with an ordinary pointer route too",
                "proper-shortcuts", [this] { launch("/usr/bin/proper-tool", {"shortcuts"}); });
        addCard(grid, 2, 0, "System Settings", "Hardware, accounts, networking, and the rest",
                "systemsettings", [this] { launch("/usr/bin/systemsettings"); });
        addCard(grid, 2, 1, "Project and support", "Read the project or report something that feels off",
                "help-about", [this] {
                    if (!QDesktopServices::openUrl(QUrl("https://github.com/marcodenic/PROPER_LINUX")))
                        showFailure("The project page could not be opened in your browser.");
                });
        grid->setColumnStretch(0, 1);
        grid->setColumnStretch(1, 1);
        root->addLayout(grid, 1);

        auto *footer = new QLabel("Proper Linux 0.1 · Normal system controls stay available");
        footer->setObjectName("guideFooter");
        footer->setAlignment(Qt::AlignCenter);
        footer->setWordWrap(true);
        root->addWidget(footer);
    }

private:
    void addCard(QGridLayout *grid, int row, int column, const QString &title,
                 const QString &description, const QString &icon,
                 std::function<void()> action) {
        auto *button = new QPushButton(title + "\n" + description);
        button->setObjectName("guideCard");
        button->setIcon(properIcon(icon));
        button->setIconSize(QSize(42, 42));
        button->setCursor(Qt::PointingHandCursor);
        button->setAccessibleName(title + ". " + description);
        button->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        connect(button, &QPushButton::clicked, this, [action = std::move(action)] { action(); });
        grid->addWidget(button, row, column);
    }

    void launch(const QString &program, const QStringList &arguments = {}) {
        if (!QProcess::startDetached(program, arguments))
            showFailure("That tool could not be opened. Reinstall the corresponding Proper Linux package and try again.");
    }

    void showFailure(const QString &message) {
        status->setText(message);
        status->show();
    }

    QLabel *status = nullptr;
};

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    if (QIcon::themeName().isEmpty())
        QIcon::setThemeName("breeze");
    QApplication::setApplicationName("Proper Welcome");
    QApplication::setDesktopFileName("org.properlinux.Welcome");

    const int screenshotOption = application.arguments().indexOf("--screenshot");
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
