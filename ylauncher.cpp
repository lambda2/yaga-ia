#include "ylauncher.h"

YLauncher::YLauncher(QStringList args)
{
	this->input = new QStringList(args);
}

QString YLauncher::printStack()
{
	return (this->input->join(' '));
}
