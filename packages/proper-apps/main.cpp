#include <QApplication>
#include <QButtonGroup>
#include <QComboBox>
#include <QDesktopServices>
#include <QDialog>
#include <QDialogButtonBox>
#include <QDir>
#include <QFile>
#include <QFileDialog>
#include <QFileInfo>
#include <QFormLayout>
#include <QFrame>
#include <QHBoxLayout>
#include <QIcon>
#include <QImageReader>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QLabel>
#include <QLayout>
#include <QLineEdit>
#include <QMessageBox>
#include <QMouseEvent>
#include <QPainter>
#include <QProcess>
#include <QProcessEnvironment>
#include <QProgressBar>
#include <QPushButton>
#include <QRegularExpression>
#include <QSaveFile>
#include <QScrollArea>
#include <QSet>
#include <QStackedWidget>
#include <QStandardPaths>
#include <QTextBrowser>
#include <QToolButton>
#include <QUuid>
#include <QVBoxLayout>
#include <QWidgetItem>

class FlowLayout final : public QLayout {
public:
    explicit FlowLayout(QWidget *parent = nullptr, int margin = 0, int horizontal = 16, int vertical = 16)
        : QLayout(parent), horizontalSpacing(horizontal), verticalSpacing(vertical) {
        setContentsMargins(margin, margin, margin, margin);
    }

    ~FlowLayout() override {
        while (auto *item = takeAt(0))
            delete item;
    }

    void addItem(QLayoutItem *item) override { items.append(item); }
    int count() const override { return items.size(); }
    QLayoutItem *itemAt(int index) const override { return items.value(index); }
    QLayoutItem *takeAt(int index) override {
        return index >= 0 && index < items.size() ? items.takeAt(index) : nullptr;
    }
    Qt::Orientations expandingDirections() const override { return {}; }
    bool hasHeightForWidth() const override { return true; }
    int heightForWidth(int width) const override { return doLayout(QRect(0, 0, width, 0), true); }
    QSize minimumSize() const override {
        QSize size;
        for (const auto *item : items)
            size = size.expandedTo(item->minimumSize());
        const auto margins = contentsMargins();
        return size + QSize(margins.left() + margins.right(), margins.top() + margins.bottom());
    }
    QSize sizeHint() const override { return minimumSize(); }
    void setGeometry(const QRect &rect) override {
        QLayout::setGeometry(rect);
        doLayout(rect, false);
    }

private:
    int doLayout(const QRect &rect, bool testOnly) const {
        const auto margins = contentsMargins();
        const QRect area = rect.adjusted(margins.left(), margins.top(), -margins.right(), -margins.bottom());
        int x = area.x();
        int y = area.y();
        int lineHeight = 0;
        for (QLayoutItem *item : items) {
            const int nextX = x + item->sizeHint().width() + horizontalSpacing;
            if (nextX - horizontalSpacing > area.right() && lineHeight > 0) {
                x = area.x();
                y += lineHeight + verticalSpacing;
                lineHeight = 0;
            }
            if (!testOnly)
                item->setGeometry(QRect(QPoint(x, y), item->sizeHint()));
            x += item->sizeHint().width() + horizontalSpacing;
            lineHeight = qMax(lineHeight, item->sizeHint().height());
        }
        return y + lineHeight - rect.y() + margins.bottom();
    }

    QList<QLayoutItem *> items;
    int horizontalSpacing;
    int verticalSpacing;
};

static QString homePath() {
    return QDir::homePath();
}

static QString expandToken(QString value) {
    return value.replace("{home}", homePath());
}

static QStringList jsonStrings(const QJsonArray &values) {
    QStringList result;
    for (const auto &value : values)
        result << expandToken(value.toString());
    return result;
}

static QString initialsFor(const QString &name) {
    const auto words = name.split(QRegularExpression("\\s+"), Qt::SkipEmptyParts);
    if (words.size() > 1)
        return (words.first().left(1) + words.last().left(1)).toUpper();
    return name.left(name.size() > 3 ? 2 : 3).toUpper();
}

static QIcon catalogueIcon(const QJsonObject &entry, int size = 72) {
    const QString id = entry.value("id").toString();
    const QStringList roots = {
        "/usr/share/proper-apps/icons",
        QDir::current().absoluteFilePath("packages/proper-apps/icons"),
        QDir::current().absoluteFilePath("icons")
    };
    for (const QString &root : roots) {
        for (const QString &extension : {QStringLiteral("png"), QStringLiteral("svg"), QStringLiteral("webp")}) {
            const QString path = root + "/" + id + "." + extension;
            if (!QFileInfo::exists(path))
                continue;
            const QIcon artwork(path);
            if (!artwork.isNull())
                return artwork;
        }
    }

    const QIcon themed = QIcon::fromTheme(entry.value("icon").toString());
    if (!themed.isNull())
        return themed;

    QPixmap pixmap(size, size);
    pixmap.fill(Qt::transparent);
    QPainter painter(&pixmap);
    painter.setRenderHint(QPainter::Antialiasing);
    const QColor accent(entry.value("accent").toString("#4c8bf5"));
    QLinearGradient gradient(0, 0, size, size);
    gradient.setColorAt(0, accent.lighter(118));
    gradient.setColorAt(1, accent.darker(118));
    painter.setBrush(gradient);
    painter.setPen(QPen(QColor(255, 255, 255, 35), 1));
    painter.drawRoundedRect(QRectF(1, 1, size - 2, size - 2), size * 0.25, size * 0.25);
    QFont font = painter.font();
    font.setBold(true);
    font.setPixelSize(size * 0.31);
    painter.setFont(font);
    painter.setPen(Qt::white);
    painter.drawText(pixmap.rect(), Qt::AlignCenter, initialsFor(entry.value("name").toString()));
    return QIcon(pixmap);
}

class AppCard final : public QFrame {
    Q_OBJECT
public:
    AppCard(const QJsonObject &entry, bool installed, QWidget *parent = nullptr)
        : QFrame(parent), id(entry.value("id").toString()) {
        setObjectName("appCard");
        setFixedSize(252, 224);
        setCursor(Qt::PointingHandCursor);
        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(18, 16, 18, 15);
        root->setSpacing(8);

        auto *top = new QHBoxLayout;
        auto *icon = new QLabel;
        icon->setPixmap(catalogueIcon(entry).pixmap(54, 54));
        icon->setFixedSize(56, 56);
        top->addWidget(icon);
        top->addStretch();
        auto *category = new QLabel(entry.value("category").toString().toUpper());
        category->setObjectName("categoryPill");
        top->addWidget(category, 0, Qt::AlignTop);
        root->addLayout(top);

        auto *name = new QLabel(entry.value("name").toString());
        name->setObjectName("cardTitle");
        name->setWordWrap(true);
        root->addWidget(name);
        auto *description = new QLabel(entry.value("description").toString());
        description->setObjectName("cardDescription");
        description->setWordWrap(true);
        description->setMaximumHeight(50);
        root->addWidget(description);
        root->addStretch();

        auto *bottom = new QHBoxLayout;
        auto *details = new QToolButton;
        details->setText("Details");
        details->setObjectName("quietButton");
        details->setCursor(Qt::PointingHandCursor);
        bottom->addWidget(details);
        bottom->addStretch();
        auto *action = new QPushButton;
        action->setCursor(Qt::PointingHandCursor);
        const bool launchable = !entry.value("launch_args").toArray().isEmpty();
        action->setText(installed ? (launchable ? "Open" : "Installed") : "Install");
        action->setEnabled(!installed || launchable);
        action->setObjectName(installed ? "secondaryButton" : "primaryButton");
        bottom->addWidget(action);
        root->addLayout(bottom);

        connect(details, &QToolButton::clicked, this, [this] { emit detailsRequested(id); });
        connect(action, &QPushButton::clicked, this, [this] { emit primaryRequested(id); });
    }

signals:
    void primaryRequested(const QString &id);
    void detailsRequested(const QString &id);

protected:
    void mouseReleaseEvent(QMouseEvent *event) override {
        QFrame::mouseReleaseEvent(event);
        if (rect().contains(event->position().toPoint()))
            emit detailsRequested(id);
    }

private:
    QString id;
};

class WebCard final : public QFrame {
    Q_OBJECT
public:
    explicit WebCard(const QJsonObject &entry, QWidget *parent = nullptr)
        : QFrame(parent), id(entry.value("id").toString()) {
        setObjectName("appCard");
        setFixedSize(252, 196);
        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(18, 16, 18, 15);
        root->setSpacing(8);
        auto *top = new QHBoxLayout;
        auto *icon = new QLabel;
        const QString iconPath = entry.value("icon_path").toString();
        QIcon webIcon = iconPath.isEmpty() ? QIcon::fromTheme("web-browser") : QIcon(iconPath);
        if (webIcon.isNull()) {
            QJsonObject fallback{{"name", entry.value("name")}, {"accent", "#3978c5"}};
            webIcon = catalogueIcon(fallback);
        }
        icon->setPixmap(webIcon.pixmap(54, 54));
        icon->setFixedSize(56, 56);
        top->addWidget(icon);
        top->addStretch();
        auto *label = new QLabel("WEB APP");
        label->setObjectName("categoryPill");
        top->addWidget(label, 0, Qt::AlignTop);
        root->addLayout(top);
        auto *name = new QLabel(entry.value("name").toString());
        name->setObjectName("cardTitle");
        root->addWidget(name);
        auto *host = new QLabel(QUrl(entry.value("url").toString()).host());
        host->setObjectName("cardDescription");
        root->addWidget(host);
        root->addStretch();
        auto *actions = new QHBoxLayout;
        auto *remove = new QToolButton;
        remove->setText("Remove");
        remove->setObjectName("quietButton");
        auto *open = new QPushButton("Open");
        open->setObjectName("secondaryButton");
        actions->addWidget(remove);
        actions->addStretch();
        actions->addWidget(open);
        root->addLayout(actions);
        connect(open, &QPushButton::clicked, this, [this] { emit openRequested(id); });
        connect(remove, &QToolButton::clicked, this, [this] { emit removeRequested(id); });
    }

signals:
    void openRequested(const QString &id);
    void removeRequested(const QString &id);

private:
    QString id;
};

class ProperApps final : public QWidget {
    Q_OBJECT
public:
    ProperApps() {
        setObjectName("root");
        setWindowTitle("Proper Apps");
        setWindowIcon(QIcon::fromTheme("system-software-install"));
        resize(1180, 760);
        setMinimumSize(720, 500);
        buildUi();
        loadCatalogue();
        loadWebApps();
        refreshInstalledState();
        populateCategories();
        refresh();
    }

private:
    void buildUi() {
        setStyleSheet(R"CSS(
            QWidget#root { background: #0f151c; color: #edf3f7; }
            QLabel { color: #edf3f7; }
            QLabel#subtitle, QLabel#countLabel, QLabel#cardDescription { color: #9cacb9; }
            QLabel#cardTitle { font-size: 16px; font-weight: 650; }
            QLabel#categoryPill { color: #a9bdd0; background: #26333f; border: 1px solid #334555; border-radius: 8px; padding: 3px 7px; font-size: 9px; font-weight: 700; }
            QLineEdit, QComboBox { background: #18212a; color: #edf3f7; border: 1px solid #2b3a47; border-radius: 10px; padding: 9px 12px; selection-background-color: #3978c5; }
            QLineEdit:focus, QComboBox:focus { border: 1px solid #5b9be7; }
            QComboBox QAbstractItemView { background: #18212a; color: #edf3f7; selection-background-color: #294d70; }
            QToolButton#navButton { color: #aebbc6; background: transparent; border: 0; border-radius: 9px; padding: 9px 15px; font-weight: 600; }
            QToolButton#navButton:hover { background: #1d2832; color: #ffffff; }
            QToolButton#navButton:checked { background: #263a4d; color: #ffffff; }
            QFrame#appCard { background: #18212a; border: 1px solid #263541; border-radius: 16px; }
            QFrame#appCard:hover { background: #1c2731; border-color: #3b5367; }
            QPushButton { border-radius: 9px; padding: 7px 14px; font-weight: 650; }
            QPushButton#primaryButton { background: #f0f5f8; color: #111820; border: 0; }
            QPushButton#primaryButton:hover { background: #ffffff; }
            QPushButton#secondaryButton { background: #2a3a48; color: #edf3f7; border: 1px solid #3a4e60; }
            QPushButton#secondaryButton:hover { background: #34495a; }
            QPushButton:disabled { color: #71808d; background: #202a33; border-color: #2b3741; }
            QToolButton#quietButton { color: #9fb4c6; background: transparent; border: 0; padding: 6px 2px; }
            QToolButton#quietButton:hover { color: #ffffff; text-decoration: underline; }
            QScrollArea { border: 0; background: transparent; }
            QScrollArea > QWidget > QWidget { background: transparent; }
            QScrollBar:vertical { background: transparent; width: 10px; margin: 2px; }
            QScrollBar::handle:vertical { background: #334656; min-height: 34px; border-radius: 4px; }
            QScrollBar::handle:vertical:hover { background: #476176; }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: transparent; }
            QProgressBar { border: 0; border-radius: 3px; background: #26323d; min-height: 6px; max-height: 6px; }
            QProgressBar::chunk { border-radius: 3px; background: #5b9be7; }
            QLabel#banner { background: #182b3b; color: #dcecff; border: 1px solid #315271; border-radius: 10px; padding: 10px 13px; }
            QTextBrowser { background: #111820; color: #dce5eb; border: 1px solid #293845; border-radius: 10px; padding: 8px; }
            QDialog, QMessageBox { background: #0f151c; color: #edf3f7; }
        )CSS");

        auto *root = new QVBoxLayout(this);
        root->setContentsMargins(28, 24, 28, 20);
        root->setSpacing(14);
        auto *header = new QHBoxLayout;
        auto *titleBlock = new QVBoxLayout;
        auto *title = new QLabel("Proper Apps");
        QFont titleFont = title->font();
        titleFont.setPixelSize(28);
        titleFont.setBold(true);
        title->setFont(titleFont);
        titleBlock->addWidget(title);
        auto *subtitle = new QLabel("Excellent software, one dependable install path.");
        subtitle->setObjectName("subtitle");
        titleBlock->addWidget(subtitle);
        header->addLayout(titleBlock);
        header->addStretch();
        search = new QLineEdit;
        search->setPlaceholderText("Search apps");
        search->setClearButtonEnabled(true);
        search->setFixedWidth(320);
        header->addWidget(search, 0, Qt::AlignBottom);
        root->addLayout(header);

        auto *navRow = new QHBoxLayout;
        navGroup = new QButtonGroup(this);
        navGroup->setExclusive(true);
        const QStringList views = {"Recommended", "Installed", "All", "Web apps"};
        for (int i = 0; i < views.size(); ++i) {
            auto *button = new QToolButton;
            button->setText(views[i]);
            button->setCheckable(true);
            button->setObjectName("navButton");
            button->setCursor(Qt::PointingHandCursor);
            navGroup->addButton(button, i);
            navRow->addWidget(button);
            if (i == 0)
                button->setChecked(true);
        }
        navRow->addStretch();
        category = new QComboBox;
        category->setMinimumWidth(176);
        navRow->addWidget(category);
        countLabel = new QLabel;
        countLabel->setObjectName("countLabel");
        navRow->addWidget(countLabel);
        root->addLayout(navRow);

        banner = new QLabel;
        banner->setObjectName("banner");
        banner->setWordWrap(true);
        banner->setVisible(false);
        root->addWidget(banner);
        operationProgress = new QProgressBar;
        operationProgress->setVisible(false);
        root->addWidget(operationProgress);
        stack = new QStackedWidget;
        root->addWidget(stack, 1);

        auto *cataloguePage = new QWidget;
        auto *catalogueLayout = new QVBoxLayout(cataloguePage);
        catalogueLayout->setContentsMargins(0, 4, 0, 0);
        catalogueScroll = new QScrollArea;
        catalogueScroll->setWidgetResizable(true);
        catalogueScroll->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        catalogueGrid = new QWidget;
        catalogueFlow = new FlowLayout(catalogueGrid, 2, 16, 16);
        catalogueScroll->setWidget(catalogueGrid);
        catalogueLayout->addWidget(catalogueScroll);
        stack->addWidget(cataloguePage);

        auto *webPage = new QWidget;
        auto *webLayout = new QVBoxLayout(webPage);
        webLayout->setContentsMargins(0, 4, 0, 0);
        auto *webHero = new QFrame;
        webHero->setObjectName("appCard");
        auto *heroLayout = new QHBoxLayout(webHero);
        heroLayout->setContentsMargins(20, 16, 20, 16);
        auto *heroText = new QVBoxLayout;
        auto *heroTitle = new QLabel("Turn any website into an app");
        heroTitle->setObjectName("cardTitle");
        auto *heroDescription = new QLabel("Give it a name and optional icon. Proper creates a removable Chromium app window and launcher entry.");
        heroDescription->setObjectName("cardDescription");
        heroDescription->setWordWrap(true);
        heroText->addWidget(heroTitle);
        heroText->addWidget(heroDescription);
        heroLayout->addLayout(heroText, 1);
        addWebAppButton = new QPushButton("Create web app");
        addWebAppButton->setObjectName("primaryButton");
        heroLayout->addWidget(addWebAppButton);
        webLayout->addWidget(webHero);
        webScroll = new QScrollArea;
        webScroll->setWidgetResizable(true);
        webScroll->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        webGrid = new QWidget;
        webFlow = new FlowLayout(webGrid, 2, 16, 16);
        webScroll->setWidget(webGrid);
        webLayout->addWidget(webScroll, 1);
        stack->addWidget(webPage);

        connect(search, &QLineEdit::textChanged, this, &ProperApps::refresh);
        connect(category, qOverload<int>(&QComboBox::currentIndexChanged), this, &ProperApps::refresh);
        connect(navGroup, &QButtonGroup::idClicked, this, [this](int id) {
            view = id;
            const bool web = id == 3;
            stack->setCurrentIndex(web ? 1 : 0);
            category->setVisible(!web);
            countLabel->setVisible(!web);
            search->setPlaceholderText(web ? "Search web apps" : "Search apps");
            refresh();
        });
        connect(addWebAppButton, &QPushButton::clicked, this, &ProperApps::createWebApp);
    }

    void loadCatalogue() {
        QStringList candidates;
        const QString override = qEnvironmentVariable("PROPER_APPS_CATALOGUE");
        if (!override.isEmpty())
            candidates << override;
        candidates << "/usr/share/proper-apps/catalogue-v2.json"
                   << QDir::current().absoluteFilePath("../../apps/catalogue-v2.json")
                   << QDir::current().absoluteFilePath("apps/catalogue-v2.json");
        for (const auto &path : candidates) {
            QFile file(path);
            if (!file.open(QIODevice::ReadOnly))
                continue;
            QJsonParseError error;
            const auto document = QJsonDocument::fromJson(file.readAll(), &error);
            if (error.error == QJsonParseError::NoError && document.isObject()) {
                entries = document.object().value("entries").toArray();
                return;
            }
        }
        banner->setText("The Proper Apps catalogue could not be loaded. Reinstall the proper-apps package and try again.");
        banner->setVisible(true);
    }

    static QString dataDirectory() { return homePath() + "/.local/share/proper-apps"; }
    static QString webAppsFile() { return dataDirectory() + "/web-apps.json"; }
    static QString webDesktopPath(const QString &id) { return homePath() + "/.local/share/applications/proper-web-" + id + ".desktop"; }

    void loadWebApps() {
        webApps = {};
        QFile file(webAppsFile());
        if (!file.open(QIODevice::ReadOnly))
            return;
        const auto document = QJsonDocument::fromJson(file.readAll());
        if (document.isObject())
            webApps = document.object().value("entries").toArray();
    }

    bool saveWebApps() {
        QDir().mkpath(dataDirectory());
        QSaveFile file(webAppsFile());
        if (!file.open(QIODevice::WriteOnly))
            return false;
        QJsonObject root;
        root.insert("version", 1);
        root.insert("entries", webApps);
        file.write(QJsonDocument(root).toJson(QJsonDocument::Indented));
        return file.commit();
    }

    static QString safeDesktopText(QString value) {
        value.replace('\n', ' ');
        value.replace('\r', ' ');
        return value.trimmed().left(120);
    }

    bool writeWebDesktop(const QJsonObject &entry) {
        const QString directory = homePath() + "/.local/share/applications";
        QDir().mkpath(directory);
        QSaveFile file(webDesktopPath(entry.value("id").toString()));
        if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
            return false;
        const QString icon = entry.value("icon_path").toString().isEmpty() ? QStringLiteral("web-browser") : entry.value("icon_path").toString();
        const QString contents = QString(
            "[Desktop Entry]\nType=Application\nVersion=1.0\nName=%1\n"
            "Comment=Web app created with Proper Apps\nExec=/usr/bin/proper-apps --launch-web-app %2\n"
            "Icon=%3\nTerminal=false\nCategories=Network;\nStartupNotify=true\nX-Proper-Web-App=true\n")
            .arg(safeDesktopText(entry.value("name").toString()), entry.value("id").toString(), icon);
        file.write(contents.toUtf8());
        if (!file.commit())
            return false;
        refreshDesktopDatabase();
        return true;
    }

    static void refreshDesktopDatabase() {
        const QString executable = QStandardPaths::findExecutable("update-desktop-database");
        if (!executable.isEmpty())
            QProcess::startDetached(executable, {homePath() + "/.local/share/applications"});
    }

    void populateCategories() {
        QSet<QString> categories;
        for (const auto &value : entries)
            categories.insert(value.toObject().value("category").toString());
        QStringList sorted(categories.begin(), categories.end());
        sorted.sort(Qt::CaseInsensitive);
        category->blockSignals(true);
        category->clear();
        category->addItem("All categories");
        category->addItems(sorted);
        category->blockSignals(false);
    }

    static void clearFlow(FlowLayout *flow) {
        while (auto *item = flow->takeAt(0)) {
            delete item->widget();
            delete item;
        }
    }

    void refresh() {
        if (view == 3) {
            refreshWebApps();
            return;
        }
        clearFlow(catalogueFlow);
        const QString query = search->text().trimmed().toLower();
        const QString selectedCategory = category->currentText();
        int shown = 0;
        for (const auto &value : entries) {
            const auto entry = value.toObject();
            const bool installed = isInstalled(entry);
            // Search the whole catalogue from the landing view so an optional
            // app never looks unavailable merely because it is not featured.
            if (view == 0 && query.isEmpty() && !entry.value("recommended").toBool())
                continue;
            if (view == 1 && !installed)
                continue;
            if (selectedCategory != "All categories" && entry.value("category").toString() != selectedCategory)
                continue;
            QString haystack = entry.value("name").toString() + " " + entry.value("description").toString() + " " + entry.value("category").toString();
            for (const auto &tag : entry.value("tags").toArray())
                haystack += " " + tag.toString();
            if (!query.isEmpty() && !haystack.toLower().contains(query))
                continue;
            auto *card = new AppCard(entry, installed);
            connect(card, &AppCard::primaryRequested, this, &ProperApps::primaryAction);
            connect(card, &AppCard::detailsRequested, this, &ProperApps::showDetails);
            catalogueFlow->addWidget(card);
            ++shown;
        }
        countLabel->setText(QString::number(shown) + (shown == 1 ? " app" : " apps"));
        if (shown == 0) {
            auto *empty = new QLabel(view == 1 ? "Nothing from the Proper catalogue is installed in this view yet." : "No applications match that search.");
            empty->setObjectName("subtitle");
            empty->setMinimumSize(420, 120);
            empty->setAlignment(Qt::AlignCenter);
            catalogueFlow->addWidget(empty);
        }
        catalogueGrid->adjustSize();
    }

    void refreshWebApps() {
        clearFlow(webFlow);
        const QString query = search->text().trimmed().toLower();
        int shown = 0;
        for (const auto &value : webApps) {
            const auto entry = value.toObject();
            if (!query.isEmpty()) {
                const QString haystack = (entry.value("name").toString() + " " + entry.value("url").toString()).toLower();
                if (!haystack.contains(query))
                    continue;
            }
            auto *card = new WebCard(entry);
            connect(card, &WebCard::openRequested, this, &ProperApps::launchWebApp);
            connect(card, &WebCard::removeRequested, this, &ProperApps::removeWebApp);
            webFlow->addWidget(card);
            ++shown;
        }
        if (shown == 0) {
            auto *empty = new QLabel(webApps.isEmpty() ? "No web apps yet. Create one for a site you use often." : "No web apps match that search.");
            empty->setObjectName("subtitle");
            empty->setMinimumSize(420, 120);
            empty->setAlignment(Qt::AlignCenter);
            webFlow->addWidget(empty);
        }
        webGrid->adjustSize();
    }

    void refreshInstalledState() {
        installedRpms.clear();
        installedFlatpaks.clear();
        QProcess rpm;
        rpm.start("/usr/bin/rpm", {"-qa", "--qf", "%{NAME}\\n"});
        if (rpm.waitForFinished(10000)) {
            const auto lines = QString::fromUtf8(rpm.readAllStandardOutput()).split('\n', Qt::SkipEmptyParts);
            installedRpms = QSet<QString>(lines.begin(), lines.end());
        }
        const QString flatpak = QStandardPaths::findExecutable("flatpak");
        if (!flatpak.isEmpty()) {
            QProcess process;
            process.start(flatpak, {"list", "--app", "--columns=application"});
            if (process.waitForFinished(15000)) {
                const auto lines = QString::fromUtf8(process.readAllStandardOutput()).split('\n', Qt::SkipEmptyParts);
                installedFlatpaks = QSet<QString>(lines.begin(), lines.end());
            }
        }
    }

    static QString resolveProgram(const QString &program) {
        if (QFileInfo(program).isAbsolute() && QFileInfo(program).isExecutable())
            return program;
        const QString local = homePath() + "/.local/bin/" + program;
        if (QFileInfo(local).isExecutable())
            return local;
        return QStandardPaths::findExecutable(program);
    }

    bool isInstalled(const QJsonObject &entry) const {
        const auto detection = entry.value("detection").toObject();
        const QString type = detection.value("type").toString();
        const QString value = detection.value("value").toString();
        if (type == "rpm") return installedRpms.contains(value);
        if (type == "flatpak") return installedFlatpaks.contains(value);
        if (type == "command") return !resolveProgram(value).isEmpty();
        return false;
    }

    QJsonObject entryFor(const QString &id) const {
        for (const auto &value : entries) {
            const auto entry = value.toObject();
            if (entry.value("id").toString() == id)
                return entry;
        }
        return {};
    }

    static QString providerName(const QString &provider) {
        if (provider == "fedora") return "Fedora";
        if (provider == "flatpak") return "Flathub";
        return "Publisher source";
    }

    void showDetails(const QString &id) {
        const auto entry = entryFor(id);
        if (entry.isEmpty()) return;
        const bool installed = isInstalled(entry);
        QDialog dialog(this);
        dialog.setWindowTitle(entry.value("name").toString() + " · Proper Apps");
        dialog.resize(590, 520);
        auto *root = new QVBoxLayout(&dialog);
        root->setContentsMargins(24, 22, 24, 22);
        root->setSpacing(14);
        auto *header = new QHBoxLayout;
        auto *icon = new QLabel;
        icon->setPixmap(catalogueIcon(entry, 88).pixmap(76, 76));
        icon->setFixedSize(78, 78);
        header->addWidget(icon, 0, Qt::AlignTop);
        auto *heading = new QVBoxLayout;
        auto *name = new QLabel(entry.value("name").toString());
        QFont nameFont = name->font();
        nameFont.setPixelSize(24);
        nameFont.setBold(true);
        name->setFont(nameFont);
        heading->addWidget(name);
        auto *meta = new QLabel(entry.value("category").toString() + "  ·  " + (installed ? "Installed" : "Available"));
        meta->setObjectName("subtitle");
        heading->addWidget(meta);
        header->addLayout(heading, 1);
        root->addLayout(header);
        auto *description = new QLabel(entry.value("description").toString());
        description->setWordWrap(true);
        root->addWidget(description);
        if (!entry.value("caveat").toString().isEmpty()) {
            auto *caveat = new QLabel(entry.value("caveat").toString());
            caveat->setObjectName("banner");
            caveat->setWordWrap(true);
            root->addWidget(caveat);
        }
        auto *website = new QPushButton("Visit website");
        website->setObjectName("secondaryButton");
        website->setMaximumWidth(140);
        connect(website, &QPushButton::clicked, &dialog, [entry] { QDesktopServices::openUrl(QUrl(entry.value("homepage").toString())); });
        root->addWidget(website);
        auto *advancedToggle = new QToolButton;
        advancedToggle->setText("Source, licence, and maintenance details");
        advancedToggle->setCheckable(true);
        advancedToggle->setObjectName("quietButton");
        advancedToggle->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);
        advancedToggle->setArrowType(Qt::RightArrow);
        root->addWidget(advancedToggle);
        auto *advanced = new QTextBrowser;
        advanced->setOpenExternalLinks(true);
        advanced->setVisible(false);
        advanced->setMaximumHeight(170);
        advanced->setHtml(QString("<b>Chosen source:</b> %1<br><b>Maintenance:</b> %2<br><b>Licence:</b> %3<br><b>Provider ID:</b> %4<br><b>Architectures:</b> %5<br><b>Last checked:</b> %6<br><a href=\"%7\">Review provider source</a>")
            .arg(providerName(entry.value("provider").toString()).toHtmlEscaped(), entry.value("status").toString().toHtmlEscaped(),
                 entry.value("license").toString().toHtmlEscaped(), entry.value("provider_id").toString().toHtmlEscaped(),
                 jsonStrings(entry.value("architectures").toArray()).join(", ").toHtmlEscaped(), entry.value("validated").toString().toHtmlEscaped(),
                 entry.value("source_url").toString().toHtmlEscaped()));
        root->addWidget(advanced);
        connect(advancedToggle, &QToolButton::toggled, &dialog, [advancedToggle, advanced](bool checked) {
            advancedToggle->setArrowType(checked ? Qt::DownArrow : Qt::RightArrow);
            advanced->setVisible(checked);
        });
        root->addStretch();
        auto *actions = new QHBoxLayout;
        auto *close = new QPushButton("Close");
        close->setObjectName("secondaryButton");
        actions->addWidget(close);
        connect(close, &QPushButton::clicked, &dialog, &QDialog::reject);
        if (installed && entry.value("removable").toBool()) {
            auto *remove = new QPushButton("Remove");
            remove->setObjectName("secondaryButton");
            actions->addWidget(remove);
            connect(remove, &QPushButton::clicked, &dialog, [this, id, &dialog] { dialog.accept(); removeEntry(id); });
        }
        actions->addStretch();
        if (installed && !entry.value("launch_args").toArray().isEmpty()) {
            auto *open = new QPushButton("Open");
            open->setObjectName("primaryButton");
            actions->addWidget(open);
            connect(open, &QPushButton::clicked, &dialog, [this, id, &dialog] { dialog.accept(); launchEntry(id); });
        } else if (!installed) {
            auto *install = new QPushButton("Install");
            install->setObjectName("primaryButton");
            actions->addWidget(install);
            connect(install, &QPushButton::clicked, &dialog, [this, id, &dialog] { dialog.accept(); installEntry(id); });
        }
        root->addLayout(actions);
        dialog.exec();
    }

    void primaryAction(const QString &id) {
        const auto entry = entryFor(id);
        if (entry.isEmpty()) return;
        if (isInstalled(entry)) launchEntry(id); else installEntry(id);
    }

    static QJsonObject step(const QString &program, const QStringList &arguments, bool privileged) {
        QJsonArray args;
        for (const auto &argument : arguments) args.append(argument);
        return QJsonObject{{"program", program}, {"args", args}, {"privileged", privileged}};
    }

    void installEntry(const QString &id) {
        const auto entry = entryFor(id);
        if (entry.isEmpty() || isInstalled(entry)) return;
        QJsonArray steps = entry.value("install_steps").toArray();
        const QString provider = entry.value("provider").toString();
        const QString providerId = entry.value("provider_id").toString();
        if (steps.isEmpty() && provider == "fedora") steps.append(step("dnf", {"install", "-y", providerId}, true));
        if (steps.isEmpty() && provider == "flatpak") {
            steps.append(step("flatpak", {"remote-add", "--user", "--if-not-exists", "flathub", "https://flathub.org/repo/flathub.flatpakrepo"}, false));
            steps.append(step("flatpak", {"install", "--user", "-y", "flathub", providerId}, false));
        }
        if (steps.isEmpty()) { showFailure("No safe installation path is configured for this entry.", {}); return; }
        startOperation(id, steps, "install");
    }

    void removeEntry(const QString &id) {
        const auto entry = entryFor(id);
        if (entry.isEmpty() || !entry.value("removable").toBool()) return;
        if (QMessageBox::question(this, "Remove " + entry.value("name").toString(), "Remove " + entry.value("name").toString() + " from this computer?") != QMessageBox::Yes) return;
        QJsonArray steps = entry.value("uninstall_steps").toArray();
        const QString provider = entry.value("provider").toString();
        const QString providerId = entry.value("provider_id").toString();
        if (steps.isEmpty() && provider == "fedora") steps.append(step("dnf", {"remove", "-y", providerId}, true));
        if (steps.isEmpty() && provider == "flatpak") steps.append(step("flatpak", {"uninstall", "--user", "-y", providerId}, false));
        if (steps.isEmpty()) { showFailure("Proper Apps does not have a safe removal path for this entry.", {}); return; }
        startOperation(id, steps, "remove");
    }

    void launchEntry(const QString &id) {
        const auto entry = entryFor(id);
        QStringList arguments = jsonStrings(entry.value("launch_args").toArray());
        if (arguments.isEmpty()) return;
        const QString programName = arguments.takeFirst();
        const QString program = resolveProgram(programName);
        if (program.isEmpty() || !QProcess::startDetached(program, arguments)) {
            showFailure("The application is installed but could not be opened.", "Executable: " + programName);
            return;
        }
        showBanner("Opened " + entry.value("name").toString() + ".");
    }

    void startOperation(const QString &id, const QJsonArray &steps, const QString &verb) {
        if (process) return;
        activeEntryId = id;
        activeSteps = steps;
        activeStep = 0;
        activeVerb = verb;
        activeOutput.clear();
        operationProgress->setRange(0, steps.size());
        operationProgress->setValue(0);
        operationProgress->setVisible(true);
        runActiveStep();
    }

    void runActiveStep() {
        const auto entry = entryFor(activeEntryId);
        if (activeStep >= activeSteps.size()) {
            operationProgress->setVisible(false);
            showBanner((activeVerb == "install" ? "Installed " : "Removed ") + entry.value("name").toString() + ".");
            activeSteps = {};
            activeEntryId.clear();
            activeVerb.clear();
            refreshInstalledState();
            refresh();
            return;
        }
        const auto current = activeSteps.at(activeStep).toObject();
        const QString programName = current.value("program").toString();
        QStringList arguments = jsonStrings(current.value("args").toArray());
        const QString program = resolveProgram(programName);
        if (program.isEmpty()) { operationFailed("Required installer component was not found.", "Missing executable: " + programName); return; }
        banner->setText((activeVerb == "install" ? "Installing " : "Removing ") + entry.value("name").toString() + QString(" · step %1 of %2").arg(activeStep + 1).arg(activeSteps.size()));
        banner->setVisible(true);
        process = new QProcess(this);
        process->setProcessChannelMode(QProcess::MergedChannels);
        auto environment = QProcessEnvironment::systemEnvironment();
        environment.insert("PATH", homePath() + "/.local/bin:" + environment.value("PATH"));
        process->setProcessEnvironment(environment);
        connect(process, &QProcess::readyRead, this, [this] {
            activeOutput += QString::fromLocal8Bit(process->readAll());
            if (activeOutput.size() > 6000) activeOutput = activeOutput.right(6000);
        });
        connect(process, &QProcess::errorOccurred, this, [this, programName](QProcess::ProcessError error) {
            if (process && error == QProcess::FailedToStart) operationFailed("The installer could not be started.", programName + ": " + process->errorString());
        });
        connect(process, qOverload<int, QProcess::ExitStatus>(&QProcess::finished), this, [this, programName](int exitCode, QProcess::ExitStatus status) {
            if (!process) return;
            activeOutput += QString::fromLocal8Bit(process->readAll());
            process->deleteLater();
            process = nullptr;
            if (status != QProcess::NormalExit || exitCode != 0) {
                operationFailed("The provider could not complete that request.", programName + QString(" exited with status %1.\n\n").arg(exitCode) + activeOutput.right(1800));
                return;
            }
            operationProgress->setValue(activeStep + 1);
            ++activeStep;
            runActiveStep();
        });
        if (current.value("privileged").toBool()) {
            const QString pkexec = resolveProgram("pkexec");
            if (pkexec.isEmpty()) {
                process->deleteLater();
                process = nullptr;
                operationFailed("System authentication is unavailable.", "pkexec was not found.");
                return;
            }
            arguments.prepend(program);
            process->start(pkexec, arguments);
        } else {
            process->start(program, arguments);
        }
    }

    void operationFailed(const QString &message, const QString &details) {
        if (process) {
            process->disconnect(this);
            process->deleteLater();
            process = nullptr;
        }
        operationProgress->setVisible(false);
        activeSteps = {};
        activeEntryId.clear();
        activeVerb.clear();
        showFailure(message, details);
        refreshInstalledState();
        refresh();
    }

    void showFailure(const QString &message, const QString &details) {
        banner->setText(message + " Nothing was assumed to be installed; you can safely try again.");
        banner->setVisible(true);
        QMessageBox box(QMessageBox::Critical, "Proper Apps", message, QMessageBox::Ok, this);
        box.setInformativeText("Check your connection and try again. Provider details are available on the application's details page.");
        if (!details.trimmed().isEmpty()) box.setDetailedText(details.right(1800));
        box.exec();
    }

    void showBanner(const QString &message) {
        banner->setText(message);
        banner->setVisible(true);
    }

    void createWebApp() {
        QDialog dialog(this);
        dialog.setWindowTitle("Create web app");
        dialog.resize(520, 280);
        auto *root = new QVBoxLayout(&dialog);
        auto *intro = new QLabel("Create a focused Chromium window and a normal launcher entry. Nothing is installed from the website.");
        intro->setWordWrap(true);
        intro->setObjectName("subtitle");
        root->addWidget(intro);
        auto *form = new QFormLayout;
        auto *name = new QLineEdit;
        name->setPlaceholderText("Notion");
        auto *url = new QLineEdit;
        url->setPlaceholderText("https://www.notion.so/");
        auto *iconPath = new QLineEdit;
        iconPath->setPlaceholderText("Optional PNG, SVG, or WebP icon");
        auto *iconRow = new QHBoxLayout;
        iconRow->addWidget(iconPath, 1);
        auto *browse = new QPushButton("Choose…");
        browse->setObjectName("secondaryButton");
        iconRow->addWidget(browse);
        form->addRow("Name", name);
        form->addRow("Website", url);
        form->addRow("Icon", iconRow);
        root->addLayout(form);
        auto *buttons = new QDialogButtonBox(QDialogButtonBox::Cancel | QDialogButtonBox::Ok);
        buttons->button(QDialogButtonBox::Ok)->setText("Create");
        buttons->button(QDialogButtonBox::Ok)->setObjectName("primaryButton");
        root->addWidget(buttons);
        connect(browse, &QPushButton::clicked, &dialog, [this, iconPath] {
            const QString selected = QFileDialog::getOpenFileName(this, "Choose web-app icon", homePath(), "Images (*.png *.jpg *.jpeg *.webp *.svg)");
            if (!selected.isEmpty()) iconPath->setText(selected);
        });
        connect(buttons, &QDialogButtonBox::rejected, &dialog, &QDialog::reject);
        connect(buttons, &QDialogButtonBox::accepted, &dialog, [&dialog, name, url, iconPath] {
            const QUrl parsed = QUrl::fromUserInput(url->text().trimmed());
            if (name->text().trimmed().isEmpty() || name->text().trimmed().size() > 60) {
                QMessageBox::warning(&dialog, "Create web app", "Enter a name between 1 and 60 characters."); return;
            }
            if ((parsed.scheme() != "https" && parsed.scheme() != "http") || parsed.host().isEmpty()) {
                QMessageBox::warning(&dialog, "Create web app", "Enter a complete HTTP or HTTPS website address."); return;
            }
            if (!iconPath->text().trimmed().isEmpty()) {
                QImageReader reader(iconPath->text().trimmed());
                if (!reader.canRead()) { QMessageBox::warning(&dialog, "Create web app", "That icon file could not be read as an image."); return; }
            }
            dialog.accept();
        });
        if (dialog.exec() != QDialog::Accepted) return;

        const QString id = QUuid::createUuid().toString(QUuid::WithoutBraces);
        QString storedIcon;
        const QString selectedIcon = iconPath->text().trimmed();
        if (!selectedIcon.isEmpty()) {
            const QString iconDirectory = dataDirectory() + "/icons";
            QDir().mkpath(iconDirectory);
            QString suffix = QFileInfo(selectedIcon).suffix().toLower();
            if (suffix.isEmpty()) suffix = "png";
            storedIcon = iconDirectory + "/" + id + "." + suffix;
            if (!QFile::copy(selectedIcon, storedIcon)) { showFailure("The selected icon could not be copied.", selectedIcon); return; }
        }
        QJsonObject entry{{"id", id}, {"name", name->text().trimmed()},
            {"url", QUrl::fromUserInput(url->text().trimmed()).toString(QUrl::FullyEncoded)}, {"icon_path", storedIcon}};
        if (!writeWebDesktop(entry)) {
            if (!storedIcon.isEmpty()) QFile::remove(storedIcon);
            showFailure("The launcher entry could not be created.", webDesktopPath(id)); return;
        }
        webApps.append(entry);
        if (!saveWebApps()) {
            QFile::remove(webDesktopPath(id));
            if (!storedIcon.isEmpty()) QFile::remove(storedIcon);
            webApps.removeLast();
            showFailure("The web-app collection could not be saved.", webAppsFile()); return;
        }
        showBanner("Created " + entry.value("name").toString() + " as a web app.");
        refreshWebApps();
    }

    void launchWebApp(const QString &id) {
        if (!QProcess::startDetached("/usr/bin/proper-apps", {"--launch-web-app", id})) showFailure("The web app could not be opened.", id);
    }

    void removeWebApp(const QString &id) {
        int index = -1;
        QJsonObject entry;
        for (int i = 0; i < webApps.size(); ++i) {
            if (webApps.at(i).toObject().value("id").toString() == id) { index = i; entry = webApps.at(i).toObject(); break; }
        }
        if (index < 0) return;
        if (QMessageBox::question(this, "Remove web app", "Remove " + entry.value("name").toString() + " from the launcher?") != QMessageBox::Yes) return;
        QFile::remove(webDesktopPath(id));
        const QString iconPath = entry.value("icon_path").toString();
        const QString ownedIcons = QFileInfo(dataDirectory() + "/icons").canonicalFilePath();
        const QString ownedIcon = QFileInfo(iconPath).canonicalFilePath();
        if (!iconPath.isEmpty() && !ownedIcons.isEmpty() && ownedIcon.startsWith(ownedIcons + "/")) QFile::remove(iconPath);
        webApps.removeAt(index);
        saveWebApps();
        refreshDesktopDatabase();
        showBanner("Removed " + entry.value("name").toString() + ".");
        refreshWebApps();
    }

    QJsonArray entries;
    QJsonArray webApps;
    QSet<QString> installedRpms;
    QSet<QString> installedFlatpaks;
    int view = 0;
    QLineEdit *search = nullptr;
    QComboBox *category = nullptr;
    QLabel *countLabel = nullptr;
    QLabel *banner = nullptr;
    QProgressBar *operationProgress = nullptr;
    QButtonGroup *navGroup = nullptr;
    QStackedWidget *stack = nullptr;
    QScrollArea *catalogueScroll = nullptr;
    QWidget *catalogueGrid = nullptr;
    FlowLayout *catalogueFlow = nullptr;
    QScrollArea *webScroll = nullptr;
    QWidget *webGrid = nullptr;
    FlowLayout *webFlow = nullptr;
    QPushButton *addWebAppButton = nullptr;
    QProcess *process = nullptr;
    QJsonArray activeSteps;
    int activeStep = 0;
    QString activeEntryId;
    QString activeVerb;
    QString activeOutput;
};

static int launchWebAppFromCommandLine(const QString &id) {
    if (!QRegularExpression("^[0-9a-f-]{36}$").match(id).hasMatch()) return 2;
    QFile file(homePath() + "/.local/share/proper-apps/web-apps.json");
    if (!file.open(QIODevice::ReadOnly)) return 3;
    const auto entries = QJsonDocument::fromJson(file.readAll()).object().value("entries").toArray();
    QUrl url;
    for (const auto &value : entries) {
        const auto entry = value.toObject();
        if (entry.value("id").toString() == id) { url = QUrl(entry.value("url").toString()); break; }
    }
    if (!url.isValid() || (url.scheme() != "https" && url.scheme() != "http") || url.host().isEmpty()) return 4;
    QString browser = QStandardPaths::findExecutable("chromium-browser");
    if (browser.isEmpty()) browser = QStandardPaths::findExecutable("chromium");
    if (!browser.isEmpty()) {
        const QString windowClass = "proper-web-" + id.left(12);
        return QProcess::startDetached(browser, {"--app=" + url.toString(QUrl::FullyEncoded), "--class=" + windowClass}) ? 0 : 5;
    }
    return QDesktopServices::openUrl(url) ? 0 : 6;
}

#include "main.moc"

int main(int argc, char **argv) {
    QApplication app(argc, argv);
    QApplication::setOrganizationName("Proper Linux");
    QApplication::setApplicationName("Proper Apps");
    if (argc == 3 && QString::fromLocal8Bit(argv[1]) == "--launch-web-app")
        return launchWebAppFromCommandLine(QString::fromLocal8Bit(argv[2]));
    ProperApps window;
    window.show();
    return app.exec();
}
