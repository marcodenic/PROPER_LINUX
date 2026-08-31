#include <QApplication>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QLineEdit>
#include <QListWidget>
#include <QMessageBox>
#include <QProcess>
#include <QPushButton>
#include <QToolButton>
#include <QTextBrowser>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFile>
#include <QComboBox>
#include <QStandardPaths>
#include <QIcon>
#include <QProgressBar>

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
        advanced = new QToolButton; advanced->setText("Advanced: source, licence and maintenance"); advanced->setCheckable(true); advanced->setChecked(false); advanced->setToolButtonStyle(Qt::ToolButtonTextOnly); right->addWidget(advanced);
        sourceDetail = new QTextBrowser; sourceDetail->setVisible(false); right->addWidget(sourceDetail);
        progress = new QProgressBar; progress->setRange(0, 0); progress->setVisible(false); progress->setTextVisible(false); right->addWidget(progress);
        operation = new QLabel; operation->setWordWrap(true); operation->setVisible(false); right->addWidget(operation);
        technical = new QToolButton; technical->setText("Show technical details"); technical->setCheckable(true); technical->setVisible(false); technical->setToolButtonStyle(Qt::ToolButtonTextOnly); right->addWidget(technical);
        technicalDetail = new QTextBrowser; technicalDetail->setMaximumHeight(130); technicalDetail->setVisible(false); right->addWidget(technicalDetail);
        auto *actions = new QHBoxLayout; install = new QPushButton("Install"); launch = new QPushButton("Launch"); launch->setEnabled(false); recover = new QPushButton("Uninstall / recover"); actions->addWidget(install); actions->addWidget(launch); actions->addWidget(recover); right->addLayout(actions);
        connect(search, &QLineEdit::textChanged, this, &ProperApps::refresh);
        connect(categories, qOverload<int>(&QComboBox::currentIndexChanged), this, &ProperApps::refresh);
        connect(list, &QListWidget::currentRowChanged, this, &ProperApps::select);
        connect(install, &QPushButton::clicked, this, &ProperApps::doInstall);
        connect(launch, &QPushButton::clicked, this, &ProperApps::doLaunch);
        connect(recover, &QPushButton::clicked, this, &ProperApps::doRecover);
        connect(advanced, &QToolButton::toggled, sourceDetail, &QWidget::setVisible);
        connect(technical, &QToolButton::toggled, technicalDetail, &QWidget::setVisible);
        QFile f("/usr/share/proper-apps/catalogue-v1.json"); if (f.open(QIODevice::ReadOnly)) entries = QJsonDocument::fromJson(f.readAll()).object()["entries"].toArray();
        for (const auto &v: entries) { auto category=v.toObject()["category"].toString(); if (categories->findText(category)<0) categories->addItem(category); }
        refresh();
    }
private slots:
    void refresh() { const auto previous=current().value("id").toString(); list->clear(); auto q=search->text().toLower(); auto category=categories->currentText(); for (const auto &v: entries) { auto o=v.toObject(); auto hay=(o["name"].toString()+" "+o["category"].toString()+" "+o["description"].toString()).toLower(); if ((category=="All categories"||o["category"].toString()==category) && (q.isEmpty()||hay.contains(q))) { auto *i=new QListWidgetItem(o["name"].toString()+"  ·  "+o["category"].toString()); const auto id=o["id"].toString(); const auto iconName=id=="google-chrome"?"web-browser":id=="codex"?"applications-development":id=="btop"?"utilities-system-monitor":id=="vlc"?"video-player":id=="gnome-calculator"?"accessories-calculator":id=="docker"||id=="podman-tooling"?"package-x-generic":id=="printer-compatibility"?"printer":id.contains("vscode")?"text-editor":"applications-development"; i->setIcon(QIcon::fromTheme(iconName)); i->setData(Qt::UserRole, id); list->addItem(i); } } if (list->count()) { int row=0; for(int i=0;i<list->count();++i) if(list->item(i)->data(Qt::UserRole).toString()==previous) { row=i; break; } list->setCurrentRow(row); } else { advanced->setChecked(false); sourceDetail->clear(); detail->setHtml("<h2>No applications found</h2><p>Try another search.</p>"); install->setEnabled(false); launch->setEnabled(false); recover->setEnabled(false); } }
    QJsonObject current() const { if (!list->currentItem()) return {}; auto id=list->currentItem()->data(Qt::UserRole).toString(); for (const auto &v: entries) if (v.toObject()["id"].toString()==id) return v.toObject(); return {}; }
    bool isInstalled(const QJsonObject &o) const { const auto d=o["detection"].toObject(); const auto type=d["type"].toString(); const auto value=d["value"].toString(); if (type=="rpm") return QProcess::execute("/usr/bin/rpm", {"-q", value})==0; if (type=="flatpak") return QProcess::execute("/usr/bin/flatpak", {"info", value})==0; if (type=="command") return !QStandardPaths::findExecutable(value).isEmpty(); return false; }
    void select(int) { auto o=current(); if(o.isEmpty()) return; QStringList arch; for(auto v:o["architectures"].toArray()) arch<<v.toString(); const auto installed=isInstalled(o); const auto launchable=!o["launch_args"].toArray().isEmpty(); install->setText(installed ? "Installed" : "Install"); install->setEnabled(!installed); launch->setEnabled(installed && launchable); recover->setEnabled(installed); advanced->setChecked(false); detail->setHtml(QString("<h2>%1</h2><p>%2</p><p><b>Category:</b> %3</p><p><b>State:</b> %4</p>").arg(o["name"].toString()).arg(o["description"].toString()).arg(o["category"].toString()).arg(installed ? "Installed" : "Available")); sourceDetail->setHtml(QString("<p><b>Provider:</b> %1<br><b>Status:</b> %2<br><b>Licence:</b> %3<br><b>Architecture:</b> %4</p>").arg(o["provider"].toString(),o["status"].toString(),o["license"].toString(),arch.join(", "))); }
    void beginOperation(const QString &message, int maximum=0) { progress->setRange(0, maximum); progress->setValue(0); progress->setVisible(true); operation->setText(message); operation->setVisible(true); technical->setVisible(false); technicalDetail->clear(); technicalDetail->setVisible(false); }
    void finishOperation() { progress->setVisible(false); operation->setVisible(false); }
    void failOperation(const QString &step, QProcess *p, int code=-1) { const auto stderrText=QString::fromLocal8Bit(p->readAllStandardError()).trimmed().left(1200); const auto startError=p->errorString(); const auto status=code<0 ? QString(" Start error: %1.").arg(startError) : QString(" Exit status: %1.").arg(code); detail->setHtml(QString("<h2>Couldn’t complete that request</h2><p>Nothing was confirmed as changed. Check your connection or try again.</p><p><b>Recovery:</b> You can retry, or use Uninstall / recover if the app was partially installed.</p>")); technicalDetail->setHtml(QString("<p><b>Failed provider step:</b> %1%2<br><b>Process:</b> %3</p><pre>%4</pre>").arg(step.toHtmlEscaped(),status,p->program().toHtmlEscaped(),stderrText.toHtmlEscaped())); technical->setVisible(true); finishOperation(); install->setEnabled(true); }
    void run(QStringList args, bool privileged=false, QString success="Installed.") { if(args.isEmpty()) return; install->setEnabled(false); beginOperation("Working…"); proc=new QProcess(this); const auto step=args.first(); connect(proc, qOverload<int,QProcess::ExitStatus>(&QProcess::finished), this, [this,success,step](int code,QProcess::ExitStatus){ if(code==0) { finishOperation(); detail->setHtml(QString("<h2>%1</h2><p>The catalogue state is refreshing.</p>").arg(success)); refresh(); } else failOperation(step,proc,code); }); connect(proc,&QProcess::errorOccurred,this,[this,step](QProcess::ProcessError e){ if(e==QProcess::FailedToStart) failOperation(step,proc); }); QString program=args.takeFirst(); if(privileged) { QStringList p; p<<program<<args; proc->start("pkexec",p); } else proc->start(program,args); }
    void runSteps(const QJsonArray &steps, int index=0, const QString &success="Installed.") { if(index>=steps.size()) { finishOperation(); detail->setHtml(QString("<h2>%1</h2><p>The catalogue state is refreshing.</p>").arg(success)); refresh(); install->setEnabled(true); return; } auto s=steps[index].toObject(); QString program=s["program"].toString(); QStringList args; for(auto v:s["args"].toArray()) args<<v.toString(); if(program.isEmpty()) { detail->setHtml("<h2>Couldn’t complete that request</h2><p>This provider configuration is incomplete. Try another application.</p>"); install->setEnabled(true); return; } if(index==0) beginOperation(QString("Working… step 1 of %1").arg(steps.size()), steps.size()); else { progress->setValue(index); operation->setText(QString("Working… step %1 of %2").arg(index+1).arg(steps.size())); } proc=new QProcess(this); const auto step=program+" "+args.join(" "); connect(proc, qOverload<int,QProcess::ExitStatus>(&QProcess::finished), this, [this,steps,index,success,step](int code,QProcess::ExitStatus){ if(code!=0) { failOperation(step,proc,code); return; } runSteps(steps,index+1,success); }); connect(proc,&QProcess::errorOccurred,this,[this,step](QProcess::ProcessError e){ if(e==QProcess::FailedToStart) failOperation(step,proc); }); bool privileged=s["privileged"].toBool(); if(privileged) { QStringList p; p<<program<<args; proc->start("pkexec",p); } else proc->start(program,args); }
    void doInstall(){ auto o=current(); install->setEnabled(false); auto steps=o["install_steps"].toArray(); if(!steps.isEmpty()) { runSteps(steps); return; } auto p=o["provider"].toString(); if(p=="fedora") run({"dnf","install","-y",o["provider_id"].toString()},true); else if(p=="flatpak") run({"flatpak","install","--user","-y","flathub",o["provider_id"].toString()}); else { detail->append("<p><b>Installation failed.</b> No provider adapter is configured.</p>"); install->setEnabled(true); } }
    void doLaunch(){ auto o=current(); auto a=o["launch_args"].toArray(); QStringList args; for(auto v:a) args<<v.toString(); if(args.isEmpty()) return; const auto program=args.takeFirst(); if(QProcess::startDetached(program,args)) detail->append("<p><b>Launched.</b> The application is running.</p>"); else detail->append("<p><b>Launch failed.</b> The installed application could not be started.</p>"); }
    void doRecover(){ auto o=current(); auto steps=o["uninstall_steps"].toArray(); if(!steps.isEmpty()) { runSteps(steps,0,"Removed."); return; } const auto provider=o["provider"].toString(); const auto id=o["provider_id"].toString(); if(provider=="flatpak") { run({"flatpak","uninstall","--user","-y",id},false,"Removed."); return; } if(provider=="fedora") { run({"dnf","remove","-y",id},true,"Removed."); return; } QMessageBox::information(this,"Recovery","This vendor application must be removed using its official instructions. Proper Apps stores no credentials."); }
private: QJsonArray entries; QLineEdit *search{}; QComboBox *categories{}; QListWidget *list{}; QTextBrowser *detail{},*sourceDetail{},*technicalDetail{}; QToolButton *advanced{},*technical{}; QLabel *operation{}; QProgressBar *progress{}; QPushButton *install{},*launch{},*recover{}; QProcess *proc{};
};
#include "main.moc"
int main(int argc,char **argv){ QApplication a(argc,argv); ProperApps w; w.show(); return a.exec(); }
