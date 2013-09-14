#-------------------------------------------------
#
# Project created by QtCreator 2013-09-11T09:44:36
#
#-------------------------------------------------

QT       += core

QT += sql widgets

TARGET = yaga-ia
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app


SOURCES += main.cpp \
	ylauncher.cpp \
	yabstractmanager.cpp \
	ydata.cpp \
	yjsonmanager.cpp \
	ysqlmanager.cpp

HEADERS += \
	ylauncher.h \
	yabstractmanager.h \
	ydata.h \
	yjsonmanager.h \
	ysqlmanager.h

OTHER_FILES += \
	db.json
