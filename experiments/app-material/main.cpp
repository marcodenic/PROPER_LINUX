// SPDX-License-Identifier: GPL-3.0-or-later
// Disposable feasibility study. Not packaged, registered, or used as Files.
#include <QApplication>
#include <QCheckBox>
#include <QFileSystemModel>
#include <QHBoxLayout>
#include <QLabel>
#include <QListView>
#include <QPainter>
#include <QPushButton>
#include <QShowEvent>
#include <QStandardPaths>
#include <QVBoxLayout>
#include <QWindow>
#include <KWindowEffects>

class MaterialStudy final : public QWidget {
public:
    MaterialStudy() {
        setWindowTitle("Files material study · native prototype");
        setAttribute(Qt::WA_TranslucentBackground);
        resize(1000, 640);
        setMinimumSize(650, 420);
        auto *root = new QHBoxLayout(this);
        root->setContentsMargins(0, 0, 0, 0);
        root->setSpacing(0);
        auto *navigation = new QWidget;
        navigation->setFixedWidth(220);
        auto *places = new QVBoxLayout(navigation);
        places->setContentsMargins(20, 24, 20, 24);
        places->setSpacing(12);
        places->addWidget(new QLabel("Places"));
        auto *content = new QWidget;
        content->setAutoFillBackground(true);
        auto *layout = new QVBoxLayout(content);
        layout->setContentsMargins(24, 24, 24, 24);
        heading = new QLabel;
        QFont font = heading->font();
        font.setPointSizeF(font.pointSizeF() * 1.6);
        font.setBold(true);
        heading->setFont(font);
        layout->addWidget(heading);
        model = new QFileSystemModel(this);
        model->setReadOnly(true);
        model->setFilter(QDir::AllDirs | QDir::Files | QDir::NoDotAndDotDot);
        files = new QListView;
        files->setModel(model);
        files->setViewMode(QListView::IconMode);
        files->setResizeMode(QListView::Adjust);
        files->setMovement(QListView::Static);
        files->setIconSize(QSize(56, 56));
        files->setGridSize(QSize(132, 112));
        files->setWordWrap(true);
        files->setEditTriggers(QAbstractItemView::NoEditTriggers);
        files->setFrameShape(QFrame::NoFrame);
        layout->addWidget(files, 1);
        addPlace(places, "Home", QDir::homePath());
        addPlace(places, "Documents", QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation));
        addPlace(places, "Downloads", QStandardPaths::writableLocation(QStandardPaths::DownloadLocation));
        addPlace(places, "Pictures", QStandardPaths::writableLocation(QStandardPaths::PicturesLocation));
        places->addStretch();
        frost = new QCheckBox("Frosted navigation");
        frost->setChecked(true);
        places->addWidget(frost);
        auto *note = new QLabel("Material study only.\nYour files stay read-only.");
        note->setWordWrap(true);
        places->addWidget(note);
        root->addWidget(navigation);
        root->addWidget(content, 1);
        connect(frost, &QCheckBox::toggled, this, [this] { updateMaterial(); });
        connect(files, &QListView::doubleClicked, this, [this](const QModelIndex &index) {
            if (model->isDir(index)) openDirectory(model->filePath(index));
        });
        openDirectory(QDir::homePath());
    }
protected:
    void showEvent(QShowEvent *event) override {
        QWidget::showEvent(event);
        updateMaterial();
    }
    void resizeEvent(QResizeEvent *event) override {
        QWidget::resizeEvent(event);
        updateMaterial();
    }
    void paintEvent(QPaintEvent *) override {
        QPainter painter(this);
        QColor tint = palette().color(QPalette::Window);
        tint.setAlphaF(frost->isChecked() ? 0.80 : 1.0);
        painter.setCompositionMode(QPainter::CompositionMode_Source);
        painter.fillRect(rect(), tint);
    }
private:
    void addPlace(QVBoxLayout *layout, const QString &name, const QString &path) {
        auto *button = new QPushButton(QIcon::fromTheme("folder"), name);
        button->setMinimumHeight(36);
        layout->addWidget(button);
        connect(button, &QPushButton::clicked, this, [this, path] { openDirectory(path); });
    }
    void openDirectory(const QString &path) {
        files->setRootIndex(model->setRootPath(path));
        heading->setText(path == QDir::homePath() ? "Home" : QFileInfo(path).fileName());
    }
    void updateMaterial() {
        if (windowHandle())
            KWindowEffects::enableBlurBehind(windowHandle(), frost->isChecked(), QRegion(0, 0, 220, height()));
        update();
    }
    QCheckBox *frost;
    QLabel *heading;
    QFileSystemModel *model;
    QListView *files;
};

int main(int argc, char **argv) {
    QApplication application(argc, argv);
    MaterialStudy study;
    study.show();
    return application.exec();
}
