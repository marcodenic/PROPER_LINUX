// SPDX-License-Identifier: GPL-3.0-or-later
#pragma once
#include <QDialog>
#include <QDialogButtonBox>
#include <QFile>
#include <QTextBrowser>
#include <QVBoxLayout>

class ProperHelp final : public QDialog {
public:
    explicit ProperHelp(QWidget *parent) : QDialog(parent) {
        setAttribute(Qt::WA_DeleteOnClose);
        setWindowTitle("Help · Proper Linux");
        resize(760, 640);
        auto *layout = new QVBoxLayout(this);
        layout->setContentsMargins(24, 20, 24, 20);
        auto *guide = new QTextBrowser;
        guide->setAccessibleName("Proper Linux guide");
        guide->setFrameShape(QFrame::NoFrame);
        guide->setStyleSheet("QTextBrowser { border: none; background: transparent; }");
        QFont readingFont = guide->font();
        readingFont.setPointSizeF(readingFont.pointSizeF() * 1.1);
        guide->setFont(readingFont);
        guide->document()->setDefaultStyleSheet("p { margin-top: 8px; margin-bottom: 16px; } h2 { margin-top: 24px; margin-bottom: 8px; }");
        guide->setOpenExternalLinks(true);
        QFile source(":/help.md");
        source.open(QIODevice::ReadOnly | QIODevice::Text);
        guide->setMarkdown(QString::fromUtf8(source.readAll()));
        layout->addWidget(guide, 1);
        auto *buttons = new QDialogButtonBox(QDialogButtonBox::Close);
        connect(buttons, &QDialogButtonBox::rejected, this, &QDialog::close);
        layout->addWidget(buttons);
    }
};
