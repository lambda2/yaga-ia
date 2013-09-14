#ifndef YABSTRACTMANAGER_H
#define YABSTRACTMANAGER_H

#include <QString>
#include "ydata.h"

class YAbstractManager
{
	public:
		YAbstractManager();
		virtual YData getData(QString search) = 0;

};

#endif // YABSTRACTMANAGER_H
