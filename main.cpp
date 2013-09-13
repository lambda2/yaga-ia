

#include "ylauncher.h"

using namespace std;

int main(int argc, char *argv[])
{
    YLauncher *launcher;
    QStringList vect;
    int i;

    for(i = 0; i < argc; i++)
    {
        vect << argv[i];
    }

    launcher = new YLauncher(vect);
    qDebug() << launcher->printStack();
}
