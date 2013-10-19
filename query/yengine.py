# -*- coding: utf-8 -*-
from yquery import *
from ymatcher import *
from sqlalchemy import *
from debug.debug import *
from base.ybase import *

from utils import ulist

class YEngine(YBase):

    def __init__(self, query, ctx):
        """Constructeur de notre classe"""
        YBase.__init__(self, ctx)
        self.query = YQuery(query, ctx)
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
        self.dbg("[FULL] Il y a eu {} résultat(s) !".format(entireResult.rowcount))

    def digestPartialQuery(self):
        results = []
        scheme = self.query.db.t_value
        r = self.query.searchArrayExpression(
            self.query.query.split(" "))
        if r.rowcount:
            for line in r:
                self.dbg("Résultat trouvé ARR: {}".format(line[scheme.c.sense]), 3)
                results.append(line[scheme.c.sense])
        if len(results):
            self.results.append(results)

    def changeQuery(self, newQuery):
        self.query.query = newQuery

    def digest(self):
        self.digestEntireQuery()
        self.digestPartialQuery()
        self.results = ulist.unique(self.results)
        self.dbg("[UPOST] {}".format(self.results))
        cb = self.findMatches()
        if cb:
            self.applyCallback(cb)

    def findMatches(self):
        scheme = self.query.db.t_response_scheme
        keeped = dict()
        results = dict()
        for req in self.results:
            self.dbg("req = {}".format(req))
            resq = self.query.searchMatches(req)
            if resq.rowcount :
                for r in resq:
                    keeped[r[scheme.c.pattern]] = r[scheme.c.response]
                self.dbg("##> {}".format(keeped))
            matcher = YMatcher(keeped, req, self.ctx)
            results.update(matcher.computeSchemes())
        self.dbg("[FWIN] {}\n{}".format(results, keeped))
        finalWinner = max(results, key=results.get)
        finalResponse = keeped[finalWinner]
        self.dbg("[FINALLY] {}".format(finalResponse),2)
        return self.readResponse(finalResponse)

    def readResponse(self, response_id):
        r = self.query.getResult(response_id).fetchone()
        self.routeType(r)
        return r[self.query.db.t_response.c.callback]

    def routeType(self, result):
        scheme = self.query.db.t_response_type
        scheme_r = self.query.db.t_response
        if result[scheme.c.type_name] == "text":
            self.showMessage(result[scheme_r.c.response])
        elif result[scheme.c.type_name] == "command":
            self.executeCommand(result[scheme_r.c.response])

    def showMessage(self, message):
        print(str(message).decode('latin1'))

    def executeCommand(self, command):
        pass

    def applyCallback(self, cb_id):
        response = self.readResponse(cb_id)
        while response:
            response = self.readResponse(response)
        return response