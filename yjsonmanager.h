#ifndef YJSONMANAGER_H
#define YJSONMANAGER_H

#include "yabstractmanager.h"

#include <QJsonDocument>

class YJsonManager : public YAbstractManager
{
	public:
		YJsonManager();
		YData	getData(QString search);
		bool	openDatabase();
		bool	closeDatabase();
		YData	parseData();

	private:
		QString	key;
};

#endif // YJSONMANAGER_H
