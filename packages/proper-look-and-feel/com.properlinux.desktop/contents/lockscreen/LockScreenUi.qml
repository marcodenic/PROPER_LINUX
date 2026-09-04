/*
    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
    SPDX-FileCopyrightText: 2026 Proper Linux contributors

    SPDX-License-Identifier: GPL-2.0-or-later
*/

import QtQml
import QtQuick
import QtQuick.Controls as QQC2

import org.kde.kirigami as Kirigami
import org.kde.kscreenlocker as ScreenLocker
import org.kde.plasma.components as PlasmaComponents3
import org.kde.plasma.private.keyboardindicator as KeyboardIndicator
import org.kde.plasma.private.sessions

Item {
    id: lockScreenUi

    property date currentDate: new Date()
    property bool systemMenuOpen: false
    property bool authenticationFailed: false
    property bool noPasswordConfirmation: false
    property bool authenticationVisible: false
    readonly property bool passwordVisible: authenticationVisible || passwordBox.text.length > 0 || authenticationFailed || root.notification.length > 0
    readonly property string uiFontFamily: properTokens.uiFont

    Kirigami.Theme.inherit: false
    Kirigami.Theme.colorSet: Kirigami.Theme.Complementary

    ProperTokens {
        id: properTokens
    }

    function clearEntry() {
        root.clearPassword()
        passwordBox.forceActiveFocus()
    }

    function revealAuthentication() {
        authenticationVisible = true
        Window.window.requestActivate()
        passwordBox.forceActiveFocus()
        authenticator.startAuthenticating()
        revealTimer.restart()
    }

    function recordMessage(message) {
        if (message.length === 0) {
            return
        }
        root.notification = message
        messageTimer.restart()
    }

    Component.onCompleted: {
        authenticator.startAuthenticating()
        passwordBox.forceActiveFocus()
    }

    Connections {
        target: authenticator

        function onFailed(kind) {
            if (kind !== 0) {
                return
            }
            lockScreenUi.authenticationFailed = true
            lockScreenUi.recordMessage(i18ndc("plasma_shell_org.kde.plasma.desktop", "@info:status", "Unlocking failed"))
            retryTimer.restart()
        }

        function onSucceeded() {
            if (authenticator.hadPrompt) {
                Qt.quit()
            } else {
                lockScreenUi.noPasswordConfirmation = true
                passwordBox.forceActiveFocus()
            }
        }

        function onInfoMessageChanged() {
            lockScreenUi.recordMessage(authenticator.infoMessage)
        }

        function onErrorMessageChanged() {
            lockScreenUi.recordMessage(authenticator.errorMessage)
        }

        function onPromptChanged(message) {
            lockScreenUi.recordMessage(message)
        }

        function onPromptForSecretChanged() {
            passwordBox.forceActiveFocus()
        }
    }

    SessionManagement {
        id: sessionManagement

        onAboutToSuspend: lockScreenUi.clearEntry()
    }

    KeyboardIndicator.KeyState {
        id: capsLockState
        key: Qt.Key_CapsLock
    }

    Timer {
        interval: 1000
        repeat: true
        running: true
        onTriggered: lockScreenUi.currentDate = new Date()
    }

    Timer {
        id: retryTimer
        interval: 1500
        onTriggered: {
            lockScreenUi.authenticationFailed = false
            lockScreenUi.clearEntry()
            authenticator.startAuthenticating()
        }
    }

    Timer {
        id: messageTimer
        interval: 3000
        onTriggered: root.notification = ""
    }

    Timer {
        id: revealTimer
        interval: 10000
        onTriggered: {
            if (passwordBox.text.length === 0 && !lockScreenUi.authenticationFailed && !lockScreenUi.systemMenuOpen) {
                lockScreenUi.authenticationVisible = false
            }
        }
    }

    // The quiet clock view is the idle state. Any blank-screen click must
    // reveal the authentication controls; interactive children remain above
    // this first sibling and continue to receive their own pointer events.
    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        onPressed: lockScreenUi.revealAuthentication()
    }

    Column {
        id: clock
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: parent.height * 0.15
        }
        spacing: Math.max(properTokens.spacingItem, parent.height * 0.012)

        ProperGridClock {
            anchors.horizontalCenter: parent.horizontalCenter
            cellSize: Math.min(9, Math.max(7, lockScreenUi.height * 0.0084))
            cellColor: properTokens.text
            currentDate: lockScreenUi.currentDate
            shadowColor: properTokens.alpha(properTokens.base, 0.45)
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter: parent.horizontalCenter
            color: properTokens.alpha(properTokens.text, 0.72)
            font.family: lockScreenUi.uiFontFamily
            font.pixelSize: Math.min(18, Math.max(13, lockScreenUi.height * 0.016))
            font.weight: Font.Normal
            text: Qt.formatDate(lockScreenUi.currentDate, "dddd, d MMMM")
            style: Text.Raised
            styleColor: properTokens.alpha(properTokens.base, 0.42)
        }
    }

    Item {
        id: authenticationArea
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: parent.height * 0.56 - height / 2
        }
        // One fixed visual measure keeps password length from changing the
        // composition. Only genuinely narrow screens reduce the capsule.
        width: Math.min(324, parent.width - 48)
        height: 74

        PlasmaComponents3.TextField {
            id: passwordBox
            anchors {
                left: parent.left
                right: parent.right
                top: parent.top
            }
            height: 50
            activeFocusOnTab: true
            color: "transparent"
            echoMode: TextInput.Password
            enabled: !authenticator.graceLocked && !lockScreenUi.noPasswordConfirmation
            focus: true
            font.family: lockScreenUi.uiFontFamily
            font.letterSpacing: 2.4
            font.pixelSize: 21
            horizontalAlignment: TextInput.AlignHCenter
            leftPadding: 18
            opacity: lockScreenUi.passwordVisible && !lockScreenUi.noPasswordConfirmation ? 1 : 0
            passwordCharacter: "▪"
            placeholderText: ""
            rightPadding: 18
            selectByMouse: false
            text: PasswordSync.password

            background: Rectangle {
                border.color: lockScreenUi.authenticationFailed
                    ? properTokens.alpha(properTokens.urgent, 0.62)
                    : passwordBox.activeFocus
                        ? properTokens.alpha(properTokens.accent, 0.28)
                        : properTokens.alpha(properTokens.border, 0.12)
                border.width: 1
                color: properTokens.alpha(properTokens.base, 0.38)
                radius: properTokens.controlRadius + 7

                Rectangle {
                    anchors {
                        left: parent.left
                        right: parent.right
                        top: parent.top
                        margins: 1
                    }
                    color: properTokens.alpha(properTokens.text, 0.035)
                    height: 1
                    radius: 1
                }
            }

            Behavior on opacity {
                NumberAnimation { duration: properTokens.animationFast }
            }

            onAccepted: {
                if (root.viewVisible && text.length > 0) {
                    authenticator.respond(text)
                }
            }

            onTextChanged: {
                if (text.length > 0) {
                    lockScreenUi.authenticationVisible = true
                    revealTimer.restart()
                }
            }

            Keys.onEscapePressed: {
                lockScreenUi.systemMenuOpen = false
                lockScreenUi.authenticationFailed = false
                root.notification = ""
                lockScreenUi.clearEntry()
            }

            Connections {
                target: root

                function onClearPassword() {
                    passwordBox.text = ""
                    passwordBox.text = Qt.binding(() => PasswordSync.password)
                }
            }
        }

        ProperPasswordCells {
            anchors {
                left: passwordBox.left
                right: passwordBox.right
                verticalCenter: passwordBox.verticalCenter
                leftMargin: passwordBox.leftPadding
                rightMargin: passwordBox.rightPadding
            }
            height: passwordBox.height
            opacity: passwordBox.opacity
            passwordLength: passwordBox.text.length
            visible: !lockScreenUi.noPasswordConfirmation
        }

        Binding {
            target: PasswordSync
            property: "password"
            value: passwordBox.text
        }

        PlasmaComponents3.Label {
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: passwordBox.bottom
                topMargin: 8
            }
            color: lockScreenUi.authenticationFailed
                ? properTokens.alpha(properTokens.urgent, 0.92)
                : properTokens.alpha(properTokens.text, 0.75)
            font.family: lockScreenUi.uiFontFamily
            font.pixelSize: 13
            text: capsLockState.locked
                ? i18ndc("plasma_shell_org.kde.plasma.desktop", "@info:status", "Caps Lock is on")
                : root.notification
            visible: text.length > 0
        }

        PlasmaComponents3.ToolButton {
            anchors.centerIn: passwordBox
            Accessible.name: i18ndc("plasma_shell_org.kde.plasma.desktop", "@action:button no-password unlock", "Unlock")
            display: QQC2.AbstractButton.IconOnly
            icon.name: "unlock"
            visible: lockScreenUi.noPasswordConfirmation
            onClicked: Qt.quit()
            Keys.onEnterPressed: clicked()
            Keys.onReturnPressed: clicked()
        }
    }

    Item {
        id: systemActions
        anchors {
            right: parent.right
            bottom: parent.bottom
            margins: Math.max(18, Math.min(parent.width, parent.height) * 0.034)
        }
        width: systemRow.width + moreButton.width + 8
        height: 42

        Rectangle {
            id: systemMenu
            anchors {
                right: moreButton.left
                rightMargin: 8
                verticalCenter: parent.verticalCenter
            }
            width: systemRow.width + 10
            height: 42
            border.color: properTokens.alpha(properTokens.border, 0.14)
            border.width: 1
            color: properTokens.alpha(properTokens.base, 0.42)
            opacity: lockScreenUi.systemMenuOpen ? 1 : 0
            radius: properTokens.controlRadius + 6
            visible: opacity > 0

            Behavior on opacity {
                NumberAnimation { duration: properTokens.animationFast }
            }

            Row {
                id: systemRow
                anchors.centerIn: parent
                spacing: properTokens.spacingUnit - 1

                SystemAction {
                    actionName: i18ndc("plasma_shell_org.kde.plasma.desktop", "@action:button", "Sleep")
                    callback: () => sessionManagement.suspend()
                    iconName: "system-suspend"
                    visible: sessionManagement.canSuspend
                }

                SystemAction {
                    actionName: i18ndc("plasma_shell_org.kde.plasma.desktop", "@action:button", "Switch User")
                    callback: () => sessionManagement.switchUser()
                    iconName: "system-switch-user"
                    visible: sessionManagement.canSwitchUser
                }

                SystemAction {
                    actionName: i18ndc("plasma_shell_org.kde.plasma.desktop", "@action:button", "Power")
                    callback: () => sessionManagement.requestShutdown(SessionManagement.ConfirmationMode.Skip)
                    iconName: "system-shutdown"
                    visible: sessionManagement.canShutdown
                }
            }
        }

        PlasmaComponents3.ToolButton {
            id: moreButton
            anchors {
                right: parent.right
                verticalCenter: parent.verticalCenter
            }
            width: 40
            height: 40
            Accessible.name: i18ndc("plasma_shell_org.kde.plasma.desktop", "@action:button", "System options")
            display: QQC2.AbstractButton.TextOnly
            text: "•••"

            background: Rectangle {
                border.color: properTokens.alpha(properTokens.border, 0.14)
                border.width: 1
                color: moreButton.hovered || lockScreenUi.systemMenuOpen
                    ? properTokens.alpha(properTokens.surface_alt, 0.5)
                    : properTokens.alpha(properTokens.base, 0.28)
                radius: properTokens.controlRadius + 3
            }

            contentItem: PlasmaComponents3.Label {
                color: properTokens.alpha(properTokens.text, 0.8)
                font.family: lockScreenUi.uiFontFamily
                horizontalAlignment: Text.AlignHCenter
                text: moreButton.text
                verticalAlignment: Text.AlignVCenter
            }

            onClicked: {
                lockScreenUi.systemMenuOpen = !lockScreenUi.systemMenuOpen
                if (!lockScreenUi.systemMenuOpen) {
                    passwordBox.forceActiveFocus()
                }
            }
        }
    }

    component SystemAction: PlasmaComponents3.ToolButton {
        required property string actionName
        required property var callback
        required property string iconName

        width: 36
        height: 36
        Accessible.name: actionName
        display: QQC2.AbstractButton.IconOnly
        icon.name: iconName

        background: Rectangle {
            color: parent.hovered ? properTokens.alpha(properTokens.surface_alt, 0.58) : "transparent"
            radius: properTokens.controlRadius + 1
        }

        onClicked: {
            lockScreenUi.systemMenuOpen = false
            callback()
        }
    }
}
