#include "ysqlmanager.h"

YSqlManager::YSqlManager()
{
	YSqlManager::createConnexion();
}

YData	YSqlManager::getData(QString search)
{

}

bool YSqlManager::createConnexion()
{
	QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL3");
	db.setHostName("localhost");
	db.setDatabaseName("yaga");
	db.setUserName("yaga-user");
	db.setPassword("E6s7YT7rmsZKM3ZV");
	bool ok = db.open();


	if (!ok) {
		qDebug() << "Echec de l'init bdd...";
		return false;
	}
	else
	{
		qDebug() << "Réussite de l'init bdd !";
		return true;
	}
	return false;
}
