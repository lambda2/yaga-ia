# -*- coding: utf-8 -*-
from yquery import *
from sqlalchemy import *
from debug.debug import *

class YEngine:

    def __init__(self, query):
        """Constructeur de notre classe"""
        self.query = YQuery(query)
        self.results = []
        self.__theEnd = False
        
    def isTheEnd(self):
        return self.__theEnd

    def digestEntireQuery(self):
        entireResult = self.query.searchEntireExpression()
        if entireResult.rowcount:
            self.results.append(entireResult)
        dbg("[FULL] Il y a eu {} résultat(s) !".format(entireResult.rowcount))

    def digestPartialQuery(self):
        results = []
        scheme = self.query.db.t_value
        for word in self.query.query.split(" "):
            r = self.query.searchExpression(word).fetchone()
            if r:
                dbg("Résultat trouvé : {} = {}".format(word, r[scheme.c.sense]), -1)
                results.append(r[scheme.c.sense])
        if len(results):
            self.results.append(results)

    def changeQuery(self, newQuery):
        self.query.query = newQuery

    def digest(self):
        self.digestEntireQuery()
        self.digestPartialQuery()
        dbg("[POST] {}".format(self.results), 1)