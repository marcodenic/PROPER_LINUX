#include <QApplication>
#include <QButtonGroup>
#include <QFileInfo>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QIcon>
#include <QLabel>
#include <QProcess>
#include <QPushButton>
#include <QResizeEvent>
#include <QScrollArea>
#include <QToolButton>
#include <QVBoxLayout>
#include <QVector>

struct Wallpaper {
    QString id;
    QString name;
    QString path;
};

class ProperAppearance final : public QWidget {
public:
    ProperAppearance() {
        setWindowTitle("Wallpapers");
        resize(1120, 760);
        setMinimumSize(720, 560);
        setStyleSheet(R"(
            QWidget { background: #101720; color: #edf4fb; }
            QScrollArea, QScrollArea > QWidget > QWidget { background: transparent; border: 0; }
            QToolButton {
                background: rgba(27, 39, 52, 0.92);
                border: 1px solid rgba(206, 226, 245, 0.13);
                border-radius: 15px;
                color: rgba(242, 247, 252, 0.86);
                font-size: 15px;
                padding: 10px;
            }
            QToolButton:hover { background: rgba(36, 53, 70, 0.96); border-color: rgba(145, 196, 239, 0.38); }
            QToolButton:checked { background: rgba(27, 54, 78, 0.98); border: 2px solid #78b9ee; color: white; }
            QPushButton {
                background: rgba(37, 52, 67, 0.96);
                border: 1px solid rgba(206, 226, 245, 0.16);
                border-radius: 10px;
                color: white;
                min-height: 38px;
                padding: 0 18px;
            }
            QPushButton:hover { background: rgba(51, 70, 88, 1); }
            QPushButton#primary { background: #4e91ca; border-color: #75b8ed; }
            QPushButton#primary:hover { background: #5aa1dc; }
            QLabel#status { color: rgba(226, 237, 247, 0.66); }
        )");

        wallpapers = {
            {"ProperBlueHour", "Proper Blue Hour", "/usr/share/wallpapers/ProperBlueHour/contents/images/1920x1080.png"},
            {"ProperHorizon", "Proper Horizon", "/usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png"},
            {"Path", "Path", "/usr/share/wallpapers/Path/contents/images/2560x1600.jpg"},
            {"Volna", "Volna", "/usr/share/wallpapers/Volna/contents/images/5120x2880.jpg"},
            {"summer_1am", "Summer 1 AM", "/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg"},
        };

        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(28, 24, 28, 24);
        root->setSpacing(16);

        auto *title = new QLabel("<h1>Wallpapers</h1><p>Five calm, hand-picked backgrounds for Proper Linux.</p>");
        root->addWidget(title);

        auto *scroll = new QScrollArea;
        scroll->setWidgetResizable(true);
        scroll->setFrameShape(QFrame::NoFrame);
        gallery = new QWidget;
        grid = new QGridLayout(gallery);
        grid->setContentsMargins(0, 0, 0, 0);
        grid->setHorizontalSpacing(18);
        grid->setVerticalSpacing(18);
        scroll->setWidget(gallery);
        root->addWidget(scroll, 1);

        group = new QButtonGroup(this);
        group->setExclusive(true);
        for (int index = 0; index < wallpapers.size(); ++index) {
            const auto &wallpaper = wallpapers[index];
            auto *card = new QToolButton;
            card->setText(wallpaper.name);
            card->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
            card->setCheckable(true);
            card->setMinimumSize(280, 190);
            card->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
            card->setIconSize(QSize(300, 160));
            if (QFileInfo::exists(wallpaper.path)) {
                card->setIcon(QIcon(wallpaper.path));
            }
            group->addButton(card, index);
            cards.append(card);
        }
        cards.first()->setChecked(true);
        rebuildGrid();

        status = new QLabel("Desktop and lock screen change together. Login sync asks for administrator approval.");
        status->setObjectName("status");
        status->setWordWrap(true);
        root->addWidget(status);

        auto *actions = new QHBoxLayout;
        actions->addStretch();
        auto *applyButton = new QPushButton("Use wallpaper");
        auto *everywhereButton = new QPushButton("Use everywhere");
        everywhereButton->setObjectName("primary");
        everywhereButton->setIcon(QIcon::fromTheme("security-high"));
        actions->addWidget(applyButton);
        actions->addWidget(everywhereButton);
        root->addLayout(actions);

        connect(applyButton, &QPushButton::clicked, this, [this] { applySelected(false); });
        connect(everywhereButton, &QPushButton::clicked, this, [this] { applySelected(true); });
    }

protected:
    void resizeEvent(QResizeEvent *event) override {
        QWidget::resizeEvent(event);
        const int wantedColumns = event->size().width() >= 980 ? 3 : event->size().width() >= 680 ? 2 : 1;
        if (wantedColumns != columns) {
            columns = wantedColumns;
            rebuildGrid();
        }
    }

private:
    void rebuildGrid() {
        while (auto *item = grid->takeAt(0)) {
            delete item;
        }
        for (int index = 0; index < cards.size(); ++index) {
            grid->addWidget(cards[index], index / columns, index % columns);
        }
        grid->setRowStretch((cards.size() + columns - 1) / columns, 1);
    }

    void applySelected(bool syncLogin) {
        const int index = group->checkedId();
        if (index < 0 || index >= wallpapers.size()) {
            return;
        }
        const auto &wallpaper = wallpapers[index];
        if (!QFileInfo::exists(wallpaper.path)) {
            status->setText("That wallpaper is missing. Reinstall Proper Linux artwork and try again.");
            return;
        }
        const int result = QProcess::execute("/usr/bin/plasma-apply-wallpaperimage", {wallpaper.path});
        if (result != 0) {
            status->setText("The wallpaper could not be applied. Your previous wallpaper is unchanged.");
            return;
        }
        status->setText(QString("%1 now appears on the desktop and lock screen.").arg(wallpaper.name));
        if (!syncLogin) {
            return;
        }

        status->setText(QString("%1 is applied. Approve the prompt to use it on the login screen too.").arg(wallpaper.name));
        auto *process = new QProcess(this);
        connect(process, qOverload<int, QProcess::ExitStatus>(&QProcess::finished), this,
                [this, process, wallpaper](int code, QProcess::ExitStatus) {
            status->setText(code == 0
                ? QString("%1 is now the desktop, lock-screen, and login wallpaper.").arg(wallpaper.name)
                : QString("Desktop and lock screen changed, but login sync was cancelled or failed."));
            process->deleteLater();
        });
        process->start("/usr/bin/pkexec", {"/usr/libexec/proper-set-login-wallpaper", wallpaper.id});
    }

    QVector<Wallpaper> wallpapers;
    QVector<QToolButton *> cards;
    QButtonGroup *group = nullptr;
    QWidget *gallery = nullptr;
    QGridLayout *grid = nullptr;
    QLabel *status = nullptr;
    int columns = 3;
};

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    ProperAppearance window;
    window.show();
    return application.exec();
}
