#include <QApplication>
#include <QCloseEvent>
#include <QFontDatabase>
#include <QHBoxLayout>
#include <QLabel>
#include <QLinearGradient>
#include <QPainter>
#include <QProcess>
#include <QPushButton>
#include <QScreen>
#include <QTimer>
#include <QVBoxLayout>

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
        setWindowTitle("Welcome to Proper Linux");
        setWindowIcon(QIcon::fromTheme("proper-logo-icon"));
        setMinimumSize(760, 540);
        setStyleSheet(R"(
            QWidget { color: #f3f6fa; background: transparent; font-family: "Noto Sans"; }
            QLabel#eyebrow { color: #8e9aaa; font-size: 11px; font-weight: 700; letter-spacing: 2px; }
            QLabel#headline { color: #f7f8fa; font-size: 31px; font-weight: 650; }
            QLabel#body { color: #9da8b5; font-size: 15px; line-height: 1.45; }
            QLabel#liveBadge {
                color: #b8cee5; background: rgba(70, 108, 148, 0.18);
                border: 1px solid rgba(145, 188, 229, 0.24); border-radius: 13px;
                font-size: 11px; font-weight: 650; padding: 5px 10px;
            }
            QLabel#footer { color: rgba(206, 217, 228, 0.46); font-size: 11px; }
            QPushButton {
                min-height: 48px; min-width: 176px; padding: 0 24px;
                border-radius: 12px; border: 1px solid rgba(204, 221, 238, 0.17);
                background: rgba(25, 34, 46, 0.88); color: #f4f7fa;
                font-family: "Noto Sans"; font-size: 14px; font-weight: 600;
            }
            QPushButton:hover { background: rgba(38, 51, 67, 0.96); border-color: rgba(155, 199, 241, 0.42); }
            QPushButton:focus { border: 2px solid #9bc7f1; }
            QPushButton#primary { background: #edf3f9; color: #111720; border-color: #ffffff; }
            QPushButton#primary:hover { background: #ffffff; }
            QPushButton#close {
                min-width: 38px; max-width: 38px; min-height: 38px; max-height: 38px;
                padding: 0; border-radius: 19px; font-size: 22px; font-weight: 400;
                color: #aeb9c5; background: rgba(20, 28, 38, .55);
            }
        )");

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
        headline->setMinimumHeight(46);
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

        auto *footer = new QLabel("Proper Linux 0.1  ·  Built on Fedora Linux and KDE Plasma");
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

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    QApplication::setApplicationName("Proper Welcome");
    QApplication::setDesktopFileName("org.properlinux.Welcome");

    if (application.arguments().contains("--install"))
        return QProcess::startDetached("/usr/bin/liveinst", {}) ? 0 : 1;

    Welcome window;
    const int screenshotOption = application.arguments().indexOf("--screenshot");
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
