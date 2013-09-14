#ifndef YLAUNCHER_H
#define YLAUNCHER_H

#include <QString>
#include <QStringList>
#include <QDebug>

#include <iostream>
#include <string>

#include "ysqlmanager.h"

class YLauncher
{

	private:
		QStringList			*input;
		YAbstractManager	*manager;

	public:
		YLauncher(QStringList args);
		QString				printStack();
};

#endif // YLAUNCHER_H
