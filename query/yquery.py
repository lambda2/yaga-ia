# -*- coding: utf-8 -*-
from ydatabase import *
from sqlalchemy import *
from debug.debug import *

class YQuery:
    """Classe représentant une requete yaga"""
    def __init__(self, query):
        """Constructeur de notre classe"""
        self.query = self.cleanQuery(query)
        self.db = YDatabase()

    def cleanQuery(self, query):
        if(len(query) > 1):
            query = query[1:]
        return " ".join(query)

    def searchEntireExpression(self):
        return self.searchExpression(self.query)

    def searchExpression(self, e):
        request = self.db.getExprRequest()
        result = self.db.connection.execute(request, expr=e)
        dbg("resultats de la requete [{}]: {}".format(request, result))
        return result

    def __repr__(self):
        return "Requete actuelle: {} ({})".format(
                self.query, self.db)