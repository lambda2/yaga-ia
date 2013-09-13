#ifndef YLAUNCHER_H
#define YLAUNCHER_H

#include <QString>
#include <QStringList>
#include <QDebug>

#include <iostream>
#include <string>

class YLauncher
{

private:
    QStringList *input;

public:
    YLauncher(QStringList args);
    QString printStack();
};

#endif // YLAUNCHER_H