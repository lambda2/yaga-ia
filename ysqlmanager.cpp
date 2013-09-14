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
	QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
	db.setDatabaseName("../words.db");
	if (!db.open()) {
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
