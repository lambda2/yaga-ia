# -*- coding: utf-8 -*-
from yquery import *
from ymatcher import *
from sqlalchemy import *
from debug.debug import *
from utils import ulist

class YEngine:

    def __init__(self, query):
        """Constructeur de notre classe"""
        self.query = YQuery(query)
        self.results = []
        self.__theEnd = False
        
    def isTheEnd(self):
        return self.__theEnd

    def digestEntireQuery(self):
        scheme = self.query.db.t_value
        entireResult = self.query.searchEntireExpression()
        if entireResult.rowcount:
            for line in entireResult:
                self.results.append([line[scheme.c.sense]])
        dbg("[FULL] Il y a eu {} résultat(s) !".format(entireResult.rowcount))

    def digestPartialQuery(self):
        results = []
        scheme = self.query.db.t_value
        r = self.query.searchArrayExpression(
            self.query.query.split(" "))
        if r.rowcount:
            for line in r:
                dbg("Résultat trouvé ARR: {}".format(line[scheme.c.sense]), 3)
                results.append(line[scheme.c.sense])
        if len(results):
            self.results.append(results)

    def changeQuery(self, newQuery):
        self.query.query = newQuery

    def digest(self):
        self.digestEntireQuery()
        self.digestPartialQuery()
        dbg("[POST] {}".format(self.results), 1)
        self.results = ulist.unique(self.results)
        dbg("[UPOST] {}".format(self.results), 1)
        self.findMatches()

    def findMatches(self):
        scheme = self.query.db.t_response_scheme
        keeped = dict()
        results = dict()
        for req in self.results:
            dbg("req = {}".format(req))
            resq = self.query.searchMatches(req)
            if resq.rowcount :
                for r in resq:
                    keeped[r[scheme.c.pattern]] = r[scheme.c.response]
                dbg("##> {}".format(keeped),2)
            matcher = YMatcher(keeped, req)
            results.update(matcher.computeSchemes())
        dbg("[FWIN] {}\n{}".format(results, keeped),3)
        finalWinner = max(results)
        finalResponse = keeped[finalWinner]
        dbg("[FINALLY] {}".format(finalResponse),2)