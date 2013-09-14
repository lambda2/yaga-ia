#ifndef YABSTRACTMANAGER_H
#define YABSTRACTMANAGER_H

#include <QString>
#include "ydata.h"

class YAbstractManager
{
public:
    YAbstractManager();
    virtual YData getData(QString search);

private:

};

#endif // YABSTRACTMANAGER_H
