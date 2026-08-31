/*
    SPDX-FileCopyrightText: 2026 Proper Linux contributors
    SPDX-License-Identifier: LGPL-2.0-or-later
*/

import QtQuick
import QtQuick.Controls as QQC2
import QtQuick.Layouts

import org.kde.kirigami as Kirigami
import org.kde.plasma.components as PlasmaComponents
import org.kde.plasma.private.keyboardindicator as KeyboardIndicator

import org.kde.plasma.login as PlasmaLogin

Item {
    id: root
    anchors.fill: parent

    property date currentDate: new Date()
    property bool authenticating: false
    property bool manualUser: PlasmaLogin.GreeterState.beyondUserLimit
    property bool systemMenuOpen: false
    property int selectedUserIndex: PlasmaLogin.GreeterState.userListIndex
    property int selectedSessionIndex: PlasmaLogin.GreeterState.sessionIndex
    property string notificationMessage: ""

    readonly property int userCount: PlasmaLogin.UserModel.rowCount()
    readonly property bool uiVisible: PlasmaLogin.GreeterState.activeWindow === loginSurface.Window.window
    readonly property string selectedUsername: userData(PlasmaLogin.UserModel.NameRole)
    readonly property string selectedDisplayName: {
        const realName = userData(PlasmaLogin.UserModel.RealNameRole)
        return realName.length > 0 ? realName : selectedUsername
    }
    readonly property int selectedSessionType: sessionData(PlasmaLogin.SessionModel.TypeRole)
    readonly property string selectedSessionFileName: sessionData(PlasmaLogin.SessionModel.FileNameRole)

    Kirigami.Theme.colorSet: Kirigami.Theme.Complementary
    Kirigami.Theme.inherit: false

    Component.onCompleted: Qt.callLater(() => passwordBox.forceActiveFocus())

    function userData(role) {
        if (selectedUserIndex < 0 || selectedUserIndex >= userCount) {
            return ""
        }
        return PlasmaLogin.UserModel.data(PlasmaLogin.UserModel.index(selectedUserIndex, 0), role)
    }

    function sessionData(role) {
        if (selectedSessionIndex < 0 || selectedSessionIndex >= PlasmaLogin.SessionModel.rowCount()) {
            return ""
        }
        return PlasmaLogin.SessionModel.data(PlasmaLogin.SessionModel.index(selectedSessionIndex, 0), role)
    }

    function activate() {
        PlasmaLogin.GreeterState.activateWindow(loginSurface.Window.window)
        Qt.callLater(() => {
            if (manualUser && usernameBox.text.length === 0) {
                usernameBox.forceActiveFocus()
            } else {
                passwordBox.forceActiveFocus()
            }
        })
    }

    function clearAuthentication() {
        passwordBox.clear()
        PlasmaLogin.GreeterState.clearPasswords()
        notificationMessage = ""
        authenticating = false
    }

    function chooseUser(index) {
        selectedUserIndex = index
        manualUser = false
        PlasmaLogin.GreeterState.loginState = PlasmaLogin.GreeterState.LoginState.UserList
        PlasmaLogin.GreeterState.userListIndex = index
        clearAuthentication()
        activate()
    }

    function chooseManualUser() {
        manualUser = true
        PlasmaLogin.GreeterState.loginState = PlasmaLogin.GreeterState.LoginState.UserPrompt
        clearAuthentication()
        usernameBox.clear()
        activate()
    }

    function startLogin() {
        const username = manualUser ? usernameBox.text.trim() : selectedUsername
        if (username.length === 0 || authenticating) {
            return
        }

        notificationMessage = ""
        authenticating = true
        PlasmaLogin.GreeterState.handleLoginRequest(
            username,
            passwordBox.text,
            selectedSessionType,
            selectedSessionFileName
        )
    }

    KeyboardIndicator.KeyState {
        id: capsLockState
        key: Qt.Key_CapsLock
    }

    Timer {
        interval: 1000
        repeat: true
        running: true
        onTriggered: root.currentDate = new Date()
    }

    Timer {
        id: notificationTimer
        interval: 3000
        onTriggered: root.notificationMessage = ""
    }

    Connections {
        target: greeterEventFilter

        function onKeyPressed() {
            Qt.callLater(root.activate)
        }

        function onEscapeKeyPressed() {
            root.systemMenuOpen = false
            userMenu.dismiss()
            sessionMenu.dismiss()
            root.clearAuthentication()
            PlasmaLogin.GreeterState.timeoutWindow(loginSurface.Window.window)
        }
    }

    Connections {
        target: PlasmaLogin.GreeterState

        function onActiveWindowChanged() {
            if (root.uiVisible) {
                Qt.callLater(() => {
                    if (root.manualUser && usernameBox.text.length === 0) {
                        usernameBox.forceActiveFocus()
                    } else {
                        passwordBox.forceActiveFocus()
                    }
                })
            }
        }
    }

    Connections {
        target: PlasmaLogin.Authenticator

        function onLoginFailed() {
            root.authenticating = false
            root.notificationMessage = i18nd("plasma_login", "Login failed")
            notificationTimer.restart()
            passwordBox.selectAll()
            passwordBox.forceActiveFocus()
        }

        function onLoginSucceeded() {
            authenticationArea.opacity = 0
            systemActions.opacity = 0
        }
    }

    MouseArea {
        id: loginSurface
        anchors.fill: parent
        focus: true
        hoverEnabled: true
        cursorShape: root.uiVisible ? Qt.ArrowCursor : Qt.BlankCursor
        onPositionChanged: root.activate()
        onPressed: root.activate()

        Column {
            id: clock
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: parent.top
                topMargin: parent.height * 0.14
            }
            spacing: Math.max(8, parent.height * 0.012)

            PlasmaComponents.Label {
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#f3f8ff"
                font.pixelSize: Math.min(84, Math.max(48, root.height * 0.08))
                font.weight: Font.Normal
                text: Qt.formatTime(root.currentDate, "hh:mm")
                style: Text.Raised
                styleColor: Qt.rgba(0, 0.02, 0.06, 0.45)
            }

            PlasmaComponents.Label {
                anchors.horizontalCenter: parent.horizontalCenter
                color: Qt.rgba(0.93, 0.97, 1, 0.72)
                font.pixelSize: Math.min(17, Math.max(12, root.height * 0.015))
                font.weight: Font.Normal
                text: Qt.formatDate(root.currentDate, "dddd, d MMMM")
                style: Text.Raised
                styleColor: Qt.rgba(0, 0.02, 0.06, 0.42)
            }
        }

        Column {
            id: authenticationArea
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: parent.top
                topMargin: parent.height * 0.53
            }
            width: Math.min(330, parent.width * 0.5)
            spacing: 8
            // Keep the focused field live while the greeter is in its idle
            // state. The global event filter deliberately lets ordinary key
            // presses continue to their target, so the first character both
            // reveals the form and becomes the first password character.
            enabled: !root.authenticating
            opacity: root.uiVisible ? 1 : 0

            Behavior on opacity {
                NumberAnimation { duration: 150 }
            }

            PlasmaComponents.Label {
                anchors.horizontalCenter: parent.horizontalCenter
                color: Qt.rgba(0.94, 0.97, 1, 0.72)
                font.pixelSize: Math.min(15, Math.max(12, root.height * 0.014))
                text: root.manualUser
                    ? i18nd("plasma_login", "Other user")
                    : root.selectedDisplayName
                visible: text.length > 0
            }

            PlasmaComponents.TextField {
                id: usernameBox
                width: parent.width
                height: 46
                activeFocusOnTab: true
                color: "#f3f8ff"
                font.pixelSize: 16
                horizontalAlignment: TextInput.AlignHCenter
                placeholderText: i18nd("plasma_login", "Username")
                visible: root.manualUser

                background: Rectangle {
                    border.color: Qt.rgba(0.85, 0.92, 0.98, 0.22)
                    border.width: 1
                    color: Qt.rgba(0.02, 0.07, 0.13, 0.38)
                    radius: 13
                }

                onAccepted: passwordBox.forceActiveFocus()
            }

            PlasmaComponents.TextField {
                id: passwordBox
                width: parent.width
                height: 46
                activeFocusOnTab: true
                color: "#f3f8ff"
                echoMode: TextInput.Password
                font.pixelSize: 17
                horizontalAlignment: TextInput.AlignHCenter
                passwordCharacter: "•"
                placeholderText: ""
                selectByMouse: false

                background: Rectangle {
                    border.color: root.notificationMessage.length > 0
                        ? Qt.rgba(1, 0.45, 0.42, 0.58)
                        : Qt.rgba(0.85, 0.92, 0.98, 0.22)
                    border.width: 1
                    color: Qt.rgba(0.02, 0.07, 0.13, 0.38)
                    radius: 13
                }

                onAccepted: root.startLogin()
                onTextChanged: {
                    if (root.manualUser) {
                        PlasmaLogin.GreeterState.userPromptPassword = text
                    } else {
                        PlasmaLogin.GreeterState.userListPassword = text
                    }
                }

                Keys.onEscapePressed: {
                    root.systemMenuOpen = false
                    root.clearAuthentication()
                    PlasmaLogin.GreeterState.timeoutWindow(loginSurface.Window.window)
                }
            }

            PlasmaComponents.Label {
                anchors.horizontalCenter: parent.horizontalCenter
                color: root.notificationMessage.length > 0
                    ? Qt.rgba(1, 0.72, 0.7, 0.94)
                    : Qt.rgba(0.93, 0.97, 1, 0.74)
                font.pixelSize: 13
                text: capsLockState.locked
                    ? i18nd("plasma_login", "Caps Lock is on")
                    : root.notificationMessage
                visible: text.length > 0
            }
        }

        Item {
            id: systemActions
            anchors {
                right: parent.right
                bottom: parent.bottom
                margins: Math.max(18, Math.min(parent.width, parent.height) * 0.034)
            }
            width: systemMenu.width + moreButton.width + 8
            height: 42

            Behavior on opacity {
                NumberAnimation { duration: 150 }
            }

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
                opacity: root.systemMenuOpen ? 1 : 0
                radius: 15
                visible: opacity > 0

                Behavior on opacity {
                    NumberAnimation { duration: 130 }
                }

                Row {
                    id: systemRow
                    anchors.centerIn: parent
                    spacing: 3

                    SystemButton {
                        id: userButton
                        actionName: i18nd("plasma_login", "Choose user")
                        iconName: "system-switch-user"
                        onTriggered: {
                            sessionMenu.dismiss()
                            userMenu.popup(userButton, 0, 0)
                        }

                        PlasmaComponents.Menu {
                            id: userMenu

                            Instantiator {
                                model: PlasmaLogin.UserModel

                                onObjectAdded: (index, object) => userMenu.insertItem(index, object)
                                onObjectRemoved: (index, object) => userMenu.removeItem(object)

                                delegate: PlasmaComponents.MenuItem {
                                    required property int index
                                    required property string name
                                    required property string realName

                                    text: realName.length > 0 ? realName : name
                                    onTriggered: root.chooseUser(index)
                                }
                            }

                            PlasmaComponents.MenuSeparator {}

                            PlasmaComponents.MenuItem {
                                icon.name: "system-user-prompt"
                                text: i18nd("plasma_login", "Other user…")
                                onTriggered: root.chooseManualUser()
                            }
                        }
                    }

                    SystemButton {
                        id: sessionButton
                        actionName: i18nd("plasma_login", "Choose desktop session")
                        iconName: "preferences-desktop"
                        visible: PlasmaLogin.SessionModel.rowCount() > 1
                        onTriggered: {
                            userMenu.dismiss()
                            sessionMenu.popup(sessionButton, 0, 0)
                        }

                        PlasmaComponents.Menu {
                            id: sessionMenu

                            Instantiator {
                                model: PlasmaLogin.SessionModel

                                onObjectAdded: (index, object) => sessionMenu.insertItem(index, object)
                                onObjectRemoved: (index, object) => sessionMenu.removeItem(object)

                                delegate: PlasmaComponents.MenuItem {
                                    required property int index
                                    required property string displayName

                                    checkable: true
                                    checked: index === root.selectedSessionIndex
                                    text: displayName
                                    onTriggered: {
                                        root.selectedSessionIndex = index
                                        PlasmaLogin.GreeterState.sessionIndex = index
                                        sessionMenu.dismiss()
                                        passwordBox.forceActiveFocus()
                                    }
                                }
                            }
                        }
                    }

                    SystemButton {
                        actionName: i18nd("plasma_login", "Sleep")
                        iconName: "system-suspend"
                        visible: PlasmaLogin.SessionManagement.canSuspend
                        onTriggered: {
                            root.clearAuthentication()
                            PlasmaLogin.SessionManagement.suspend()
                        }
                    }

                    SystemButton {
                        actionName: i18nd("plasma_login", "Restart")
                        iconName: "system-reboot"
                        visible: PlasmaLogin.SessionManagement.canReboot
                        onTriggered: PlasmaLogin.SessionManagement.requestReboot(PlasmaLogin.SessionManagement.ConfirmationMode.Skip)
                    }

                    SystemButton {
                        actionName: i18nd("plasma_login", "Power off")
                        iconName: "system-shutdown"
                        visible: PlasmaLogin.SessionManagement.canShutdown
                        onTriggered: PlasmaLogin.SessionManagement.requestShutdown(PlasmaLogin.SessionManagement.ConfirmationMode.Skip)
                    }
                }
            }

            PlasmaComponents.ToolButton {
                id: moreButton
                anchors {
                    right: parent.right
                    verticalCenter: parent.verticalCenter
                }
                width: 40
                height: 40
                Accessible.name: i18nd("plasma_login", "System options")
                display: QQC2.AbstractButton.TextOnly
                text: "•••"

                background: Rectangle {
                    border.color: Qt.rgba(0.85, 0.92, 0.98, 0.14)
                    border.width: 1
                    color: moreButton.hovered || root.systemMenuOpen
                        ? Qt.rgba(0.04, 0.11, 0.19, 0.5)
                        : Qt.rgba(0.02, 0.07, 0.13, 0.28)
                    radius: 12
                }

                contentItem: PlasmaComponents.Label {
                    color: Qt.rgba(0.94, 0.97, 1, 0.8)
                    horizontalAlignment: Text.AlignHCenter
                    text: moreButton.text
                    verticalAlignment: Text.AlignVCenter
                }

                onClicked: {
                    root.activate()
                    root.systemMenuOpen = !root.systemMenuOpen
                    if (!root.systemMenuOpen) {
                        userMenu.dismiss()
                        sessionMenu.dismiss()
                        passwordBox.forceActiveFocus()
                    }
                }
            }
        }
    }

    component SystemButton: PlasmaComponents.ToolButton {
        id: systemButton

        required property string actionName
        required property string iconName
        signal triggered()

        width: 36
        height: 36
        Accessible.name: actionName
        display: QQC2.AbstractButton.IconOnly
        icon.name: iconName

        background: Rectangle {
            color: systemButton.hovered ? Qt.rgba(0.1, 0.19, 0.29, 0.58) : "transparent"
            radius: 10
        }

        onClicked: systemButton.triggered()
    }
}
