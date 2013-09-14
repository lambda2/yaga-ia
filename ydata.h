#ifndef YDATA_H
#define YDATA_H

#include <QString>
#include <QHash>

/**
 * @brief The DataType enum
 * Will simply organize the information.
 */
enum    DataType
{
    TYPE,
    WORD,
    WORD_NAME,
    WORD_CONTEXT,
    WORD_TYPE
};

/**
 * @brief Will represent all data about a word.
 */
class   YData
{

public:
    YData(QString word);

    bool    addData(DataType dt, QString str);

private:
    QString                     word;
    QHash<DataType, QString>*   word_data;

};

#endif // YDATA_H
