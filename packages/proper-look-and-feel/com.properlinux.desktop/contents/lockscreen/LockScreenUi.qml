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
    readonly property string uiFontFamily: "Inter"

    Kirigami.Theme.inherit: false
    Kirigami.Theme.colorSet: Kirigami.Theme.Complementary

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
        spacing: Math.max(8, parent.height * 0.012)

        PlasmaComponents3.Label {
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#f3f8ff"
            font.family: lockScreenUi.uiFontFamily
            font.pixelSize: Math.min(96, Math.max(52, lockScreenUi.height * 0.09))
            font.weight: Font.Normal
            text: Qt.formatTime(lockScreenUi.currentDate, "hh:mm")
            style: Text.Raised
            styleColor: Qt.rgba(0, 0.02, 0.06, 0.45)
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter: parent.horizontalCenter
            color: Qt.rgba(0.93, 0.97, 1, 0.72)
            font.family: lockScreenUi.uiFontFamily
            font.pixelSize: Math.min(18, Math.max(13, lockScreenUi.height * 0.016))
            font.weight: Font.Normal
            text: Qt.formatDate(lockScreenUi.currentDate, "dddd, d MMMM")
            style: Text.Raised
            styleColor: Qt.rgba(0, 0.02, 0.06, 0.42)
        }
    }

    Item {
        id: authenticationArea
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: parent.height * 0.56 - height / 2
        }
        width: Math.min(310, parent.width * 0.56)
        height: 70

        PlasmaComponents3.TextField {
            id: passwordBox
            anchors {
                left: parent.left
                right: parent.right
                top: parent.top
            }
            height: 46
            activeFocusOnTab: true
            color: "#f3f8ff"
            echoMode: TextInput.Password
            enabled: !authenticator.graceLocked && !lockScreenUi.noPasswordConfirmation
            focus: true
            font.family: lockScreenUi.uiFontFamily
            font.pixelSize: 17
            horizontalAlignment: TextInput.AlignHCenter
            opacity: lockScreenUi.passwordVisible && !lockScreenUi.noPasswordConfirmation ? 1 : 0
            passwordCharacter: "•"
            placeholderText: ""
            selectByMouse: false
            text: PasswordSync.password

            background: Rectangle {
                border.color: lockScreenUi.authenticationFailed
                    ? Qt.rgba(1, 0.45, 0.42, 0.55)
                    : Qt.rgba(0.85, 0.92, 0.98, 0.22)
                border.width: 1
                color: Qt.rgba(0.02, 0.07, 0.13, 0.38)
                radius: 13
            }

            Behavior on opacity {
                NumberAnimation { duration: 150 }
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
                ? Qt.rgba(1, 0.72, 0.7, 0.92)
                : Qt.rgba(0.93, 0.97, 1, 0.75)
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
            border.color: Qt.rgba(0.85, 0.92, 0.98, 0.14)
            border.width: 1
            color: Qt.rgba(0.02, 0.07, 0.13, 0.42)
            opacity: lockScreenUi.systemMenuOpen ? 1 : 0
            radius: 15
            visible: opacity > 0

            Behavior on opacity {
                NumberAnimation { duration: 130 }
            }

            Row {
                id: systemRow
                anchors.centerIn: parent
                spacing: 3

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
                    callback: () => sessionManagement.requestShutdown()
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
                border.color: Qt.rgba(0.85, 0.92, 0.98, 0.14)
                border.width: 1
                color: moreButton.hovered || lockScreenUi.systemMenuOpen
                    ? Qt.rgba(0.04, 0.11, 0.19, 0.5)
                    : Qt.rgba(0.02, 0.07, 0.13, 0.28)
                radius: 12
            }

            contentItem: PlasmaComponents3.Label {
                color: Qt.rgba(0.94, 0.97, 1, 0.8)
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
            color: parent.hovered ? Qt.rgba(0.1, 0.19, 0.29, 0.58) : "transparent"
            radius: 10
        }

        onClicked: {
            lockScreenUi.systemMenuOpen = false
            callback()
        }
    }
}
