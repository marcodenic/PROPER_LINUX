#include <QApplication>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QLineEdit>
#include <QListWidget>
#include <QMessageBox>
#include <QProcess>
#include <QPushButton>
#include <QTextBrowser>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFile>
#include <QComboBox>
#include <QStandardPaths>

class ProperApps : public QWidget {
    Q_OBJECT
public:
    ProperApps() {
        setWindowTitle("Proper Apps"); resize(920, 620);
        auto *root = new QVBoxLayout(this);
        auto *heading = new QLabel("<h1>Proper Apps</h1><p>Find the tools you need. Proper Linux handles the installation source for you.</p>");
        root->addWidget(heading);
        search = new QLineEdit; search->setPlaceholderText("Search applications"); root->addWidget(search);
        categories = new QComboBox; categories->addItem("All categories"); root->addWidget(categories);
        auto *body = new QHBoxLayout; root->addLayout(body, 1);
        list = new QListWidget; body->addWidget(list, 1);
        auto *right = new QVBoxLayout; body->addLayout(right, 2);
        detail = new QTextBrowser; right->addWidget(detail, 1);
        auto *actions = new QHBoxLayout; install = new QPushButton("Install"); launch = new QPushButton("Launch"); launch->setEnabled(false); recover = new QPushButton("Uninstall / recover"); actions->addWidget(install); actions->addWidget(launch); actions->addWidget(recover); right->addLayout(actions);
        connect(search, &QLineEdit::textChanged, this, &ProperApps::refresh);
        connect(categories, qOverload<int>(&QComboBox::currentIndexChanged), this, &ProperApps::refresh);
        connect(list, &QListWidget::currentRowChanged, this, &ProperApps::select);
        connect(install, &QPushButton::clicked, this, &ProperApps::doInstall);
        connect(launch, &QPushButton::clicked, this, &ProperApps::doLaunch);
        connect(recover, &QPushButton::clicked, this, &ProperApps::doRecover);
        QFile f("/usr/share/proper-apps/catalogue-v1.json"); if (f.open(QIODevice::ReadOnly)) entries = QJsonDocument::fromJson(f.readAll()).object()["entries"].toArray();
        for (const auto &v: entries) { auto category=v.toObject()["category"].toString(); if (categories->findText(category)<0) categories->addItem(category); }
        refresh();
    }
private slots:
    void refresh() { list->clear(); auto q=search->text().toLower(); auto category=categories->currentText(); for (const auto &v: entries) { auto o=v.toObject(); auto hay=(o["name"].toString()+" "+o["category"].toString()+" "+o["description"].toString()).toLower(); if ((category=="All categories"||o["category"].toString()==category) && (q.isEmpty()||hay.contains(q))) { auto *i=new QListWidgetItem(o["name"].toString()+"  ·  "+o["category"].toString()); i->setData(Qt::UserRole, o["id"].toString()); list->addItem(i); } } if (list->count()) list->setCurrentRow(0); else detail->setHtml("<h2>No applications found</h2><p>Try another search.</p>"); }
    QJsonObject current() const { if (!list->currentItem()) return {}; auto id=list->currentItem()->data(Qt::UserRole).toString(); for (const auto &v: entries) if (v.toObject()["id"].toString()==id) return v.toObject(); return {}; }
    bool isInstalled(const QJsonObject &o) const { const auto d=o["detection"].toObject(); const auto type=d["type"].toString(); const auto value=d["value"].toString(); if (type=="rpm") return QProcess::execute("rpm", {"-q", value})==0; if (type=="flatpak") return QProcess::execute("flatpak", {"info", value})==0; if (type=="command") return !QStandardPaths::findExecutable(value).isEmpty(); return false; }
    void select(int) { auto o=current(); if(o.isEmpty()) return; QStringList arch; for(auto v:o["architectures"].toArray()) arch<<v.toString(); const auto installed=isInstalled(o); install->setText(installed ? "Installed" : "Install"); install->setEnabled(!installed); launch->setEnabled(installed); detail->setHtml(QString("<h2>%1</h2><p>%2</p><p><b>Category:</b> %3</p><p><b>State:</b> %8</p><details><summary>Source, licence and maintenance</summary><p><b>Provider:</b> %4<br><b>Status:</b> %5<br><b>Licence:</b> %6<br><b>Architecture:</b> %7</p></details>").arg(o["name"].toString(),o["description"].toString(),o["category"].toString(),o["provider"].toString(),o["status"].toString(),o["license"].toString(),arch.join(", "),installed ? "Installed" : "Available")); }
    void run(QStringList args, bool privileged=false, QString success="Installed.") { if(args.isEmpty()) return; install->setEnabled(false); detail->append("<p><b>Working…</b></p>"); proc=new QProcess(this); connect(proc, qOverload<int,QProcess::ExitStatus>(&QProcess::finished), this, [this,success](int code,QProcess::ExitStatus){ if(code==0) { detail->append(QString("<p><b>%1</b> The catalogue state is refreshing.</p>").arg(success)); refresh(); } else detail->append("<p><b>Operation failed.</b> The provider made no confirmed change. Try again or use recovery.</p>"); install->setEnabled(true); }); QString program=args.takeFirst(); if(privileged) { QStringList p; p<<program<<args; proc->start("pkexec",p); } else proc->start(program,args); }
    void runSteps(const QJsonArray &steps, int index=0, const QString &success="Installed.") { if(index>=steps.size()) { detail->append(QString("<p><b>%1</b> The catalogue state is refreshing.</p>").arg(success)); refresh(); install->setEnabled(true); return; } auto s=steps[index].toObject(); QString program=s["program"].toString(); QStringList args; for(auto v:s["args"].toArray()) args<<v.toString(); if(program.isEmpty()) { detail->append("<p><b>Operation failed.</b> Invalid provider step.</p>"); install->setEnabled(true); return; } detail->append(QString("<p>Step %1 of %2…</p>").arg(index+1).arg(steps.size())); proc=new QProcess(this); connect(proc, qOverload<int,QProcess::ExitStatus>(&QProcess::finished), this, [this,steps,index,success](int code,QProcess::ExitStatus){ if(code!=0) { install->setEnabled(true); detail->append("<p><b>Operation failed.</b> The provider made no confirmed change. Try again or use recovery.</p>"); return; } runSteps(steps,index+1,success); }); bool privileged=s["privileged"].toBool(); if(privileged) { QStringList p; p<<program<<args; proc->start("pkexec",p); } else proc->start(program,args); }
    void doInstall(){ auto o=current(); install->setEnabled(false); auto steps=o["install_steps"].toArray(); if(!steps.isEmpty()) { runSteps(steps); return; } auto p=o["provider"].toString(); if(p=="fedora") run({"dnf","install","-y",o["provider_id"].toString()},true); else if(p=="flatpak") run({"flatpak","install","--user","-y","flathub",o["provider_id"].toString()}); else { detail->append("<p><b>Installation failed.</b> No provider adapter is configured.</p>"); install->setEnabled(true); } }
    void doLaunch(){ auto o=current(); auto a=o["launch_args"].toArray(); QStringList args; for(auto v:a) args<<v.toString(); if(args.isEmpty()) return; const auto program=args.takeFirst(); if(QProcess::startDetached(program,args)) detail->append("<p><b>Launched.</b> The application is running.</p>"); else detail->append("<p><b>Launch failed.</b> The installed application could not be started.</p>"); }
    void doRecover(){ auto o=current(); auto steps=o["uninstall_steps"].toArray(); if(!steps.isEmpty()) { runSteps(steps,0,"Removed."); return; } const auto provider=o["provider"].toString(); const auto id=o["provider_id"].toString(); if(provider=="flatpak") { run({"flatpak","uninstall","--user","-y",id},false,"Removed."); return; } if(provider=="fedora") { run({"dnf","remove","-y",id},true,"Removed."); return; } QMessageBox::information(this,"Recovery","This vendor application must be removed using its official instructions. Proper Apps stores no credentials."); }
private: QJsonArray entries; QLineEdit *search{}; QComboBox *categories{}; QListWidget *list{}; QTextBrowser *detail{}; QPushButton *install{},*launch{},*recover{}; QProcess *proc{};
};
#include "main.moc"
int main(int argc,char **argv){ QApplication a(argc,argv); ProperApps w; w.show(); return a.exec(); }
