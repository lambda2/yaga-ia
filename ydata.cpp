#include "ydata.h"

YData::YData(QString word)
{
    this->word = word;
    this->word_data = new QHash<DataType, QString>();
}

bool    YData::addData(DataType dt, QString str)
{
    this->word_data->insert(dt, str);
}
