#ifndef YDATA_H
#define YDATA_H

#include <QString>
#include <QStringList>
#include <QHash>


/**
 * @brief Will represent all data about a word.
 */
class   YData
{

	public:
		YData(QString word);

		bool    addData(QString dt, QString str);

	private:
		QString                         word;
		QHash<QString, QStringList>*    word_data;

};

#endif // YDATA_H
