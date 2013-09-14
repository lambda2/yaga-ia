#ifndef YSQLMANAGER_H
#define YSQLMANAGER_H

#include <QSqlDatabase>
#include <QSqlError>
#include <QSqlQuery>
#include <QDebug>

#include "yabstractmanager.h"


class YSqlManager : public YAbstractManager
{
	public:
		YSqlManager();
		bool	createConnexion();
		YData		getData(QString search);
};

#endif // YSQLMANAGER_H
