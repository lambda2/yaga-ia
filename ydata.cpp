#include "ydata.h"

YData::YData(QString word)
{
	this->word = word;
	this->word_data = new QHash<QString, QStringList>();
}

bool    YData::addData(QString dt, QString str)
{
	QStringList	sl;
	bool		ret;

	if ( !this->word_data->contains(dt) )
	{
		sl << str;
		ret = true;
		this->word_data->insert(dt, sl);
	}
	else
	{
		ret = false;
		sl << this->word_data->take(dt);
		this->word_data->insert(dt, sl);
	}
	return (ret);
}
