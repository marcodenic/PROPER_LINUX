// SPDX-License-Identifier: GPL-2.0-or-later
pragma ComponentBehavior: Bound
import QtQuick
import QtQuick.Controls as QQC2
import QtQuick.Layouts
import org.kde.kirigami as Kirigami
import org.kde.kcmutils as KCMUtils

KCMUtils.SimpleKCM {
    id: root
    globalToolBarStyle: Kirigami.ApplicationHeaderStyle.None
    Component.onCompleted: kcm.buttons = 0 // Navigation page: no settings to apply.
    topPadding: 24
    leftPadding: 24
    rightPadding: 24
    bottomPadding: 24
    implicitWidth: Kirigami.Units.gridUnit * 44
    implicitHeight: Kirigami.Units.gridUnit * 30

    component SettingsCard: QQC2.AbstractButton {
        id: card
        required property string title
        required property string description
        required property string symbol
        required property string module
        implicitHeight: Math.max(76, contentItem.implicitHeight + topPadding + bottomPadding)
        hoverEnabled: true
        padding: 14
        Accessible.name: title
        Accessible.description: description
        onClicked: kcm.openKCM(module)
        background: Rectangle {
            radius: 9
            color: card.hovered ? Qt.tint(Kirigami.Theme.backgroundColor, Qt.alpha(Kirigami.Theme.highlightColor, 0.08)) : Kirigami.Theme.alternateBackgroundColor
            border.width: card.visualFocus ? 2 : 0
            border.color: card.visualFocus ? Kirigami.Theme.highlightColor : Qt.alpha(Kirigami.Theme.textColor, 0.08)
        }
        contentItem: RowLayout {
            spacing: 16
            Kirigami.Icon {
                source: card.symbol
                Layout.preferredWidth: 24
                Layout.preferredHeight: 24
                color: Kirigami.Theme.textColor
            }
            ColumnLayout {
                spacing: 6
                Layout.fillWidth: true
                QQC2.Label { text: card.title; font.weight: Font.DemiBold; Layout.fillWidth: true; wrapMode: Text.Wrap }
                QQC2.Label { text: card.description; color: Qt.alpha(Kirigami.Theme.textColor, 0.72); Layout.fillWidth: true; wrapMode: Text.Wrap }
            }
            Kirigami.Icon { source: "go-next-symbolic"; Layout.preferredWidth: 16; Layout.preferredHeight: 16; opacity: 0.5 }
        }
    }

    ColumnLayout {
        spacing: 20
        Layout.maximumWidth: 820
        ColumnLayout {
            spacing: 8
            Layout.topMargin: 12
            Kirigami.Heading { text: i18n("Make it yours"); level: 1; font.pointSize: Kirigami.Theme.defaultFont.pointSize * 1.6; font.weight: Font.DemiBold }
            QQC2.Label {
                text: i18n("Your desktop, devices and everyday preferences.")
                color: Qt.alpha(Kirigami.Theme.textColor, 0.72)
                wrapMode: Text.Wrap
                Layout.fillWidth: true
            }
        }
        GridLayout {
            Layout.fillWidth: true
            columns: width < 620 ? 1 : 2
            columnSpacing: 12
            rowSpacing: 12
            SettingsCard { Layout.fillWidth: true; title: i18n("Appearance"); description: i18n("Desktop style, text size and wallpaper"); symbol: "preferences-desktop-theme-global"; module: "kcm_lookandfeel"; onClicked: kcm.openProperAppearance() }
            SettingsCard { Layout.fillWidth: true; title: i18n("Displays"); description: i18n("Resolution, scale and screen arrangement"); symbol: "preferences-desktop-display"; module: "kcm_kscreen" }
            SettingsCard { Layout.fillWidth: true; title: i18n("Sound"); description: i18n("Speakers, microphones and volume"); symbol: "preferences-desktop-sound"; module: "kcm_pulseaudio" }
            SettingsCard { Layout.fillWidth: true; title: i18n("Network"); description: i18n("Wi-Fi, Ethernet and connections"); symbol: "preferences-system-network"; module: "kcm_networkmanagement" }
            SettingsCard { Layout.fillWidth: true; title: i18n("Mouse & Touchpad"); description: i18n("Pointer speed, scrolling and gestures"); symbol: "input-mouse"; module: "kcm_mouse" }
            SettingsCard { Layout.fillWidth: true; title: i18n("Keyboard"); description: i18n("Layouts, typing and shortcuts"); symbol: "input-keyboard"; module: "kcm_keyboard" }
        }
        ColumnLayout {
            spacing: 10
            Kirigami.Heading { text: i18n("More settings"); level: 3 }
            QQC2.Label {
                text: i18n("Search above or choose a category in the sidebar. All KDE settings are available here.")
                color: Qt.alpha(Kirigami.Theme.textColor, 0.72)
                wrapMode: Text.Wrap
                Layout.fillWidth: true
            }
        }
        Item { Layout.fillHeight: true }
    }
}
