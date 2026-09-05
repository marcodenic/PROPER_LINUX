QT += widgets dbus
CONFIG += c++17
TARGET = proper-welcome
TEMPLATE = app
SOURCES += main.cpp

INCLUDEPATH += $$PWD/../proper-look-and-feel

CONFIG += link_pkgconfig
PKGCONFIG += KF6WindowSystem

RESOURCES += help.qrc
