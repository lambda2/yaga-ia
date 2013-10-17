# -*- coding: utf-8 -*-
from ydatabase import *
from sqlalchemy import *

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
        request = self.db.getExprRequest()
        result = self.db.connection.execute(request, expr=self.query)
        print("resultats de la requete [{}]: {}".format(request, result))
        for row in result:
            print "#> ", row
        
    def __repr__(self):
        return "Requete actuelle: {} ({})".format(
                self.query, self.db)