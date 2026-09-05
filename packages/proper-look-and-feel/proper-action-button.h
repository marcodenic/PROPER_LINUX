// SPDX-License-Identifier: GPL-3.0-or-later
#pragma once
#include <QLayout>
#include <QPushButton>

// A native button whose descriptive content determines its size. QPushButton's
// default hint only measures its text/icon, ignoring an installed layout.
class ProperActionButton final : public QPushButton {
public:
    using QPushButton::QPushButton;
    QSize sizeHint() const override { return layout()->sizeHint(); }
    QSize minimumSizeHint() const override { return layout()->minimumSize(); }
    bool hasHeightForWidth() const override { return layout()->hasHeightForWidth(); }
    int heightForWidth(int width) const override { return layout()->totalHeightForWidth(width); }
};
