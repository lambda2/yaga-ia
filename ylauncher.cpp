#include "ylauncher.h"

YLauncher::YLauncher(QStringList args)
{
	this->input = new QStringList(args);
	this->manager = new YSqlManager();
}

QString YLauncher::printStack()
{
	return (this->input->join(' '));
}
