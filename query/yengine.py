# -*- coding: utf-8 -*-
from yquery import *
from ymatcher import *
from sqlalchemy import *
from debug.debug import *
from base.ybase import YBase
import json

from utils import ulist

class YEngine(YBase):

    def __init__(self, query, ctx):
        """Constructeur de notre classe"""
        YBase.__init__(self, ctx)
        self.resetEngine(query)

    def resetEngine(self, query):
        self.query = YQuery(query, self.ctx)
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
        self.resetEngine(newQuery)

    def digest(self):
        self.digestEntireQuery()
        self.digestPartialQuery()
        self.results = ulist.unique(self.results)
        self.dbg("[UPOST] {}".format(self.results))
        return self.findMatches()

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
        if len(results):
            finalWinner = max(results, key=results.get)
            finalResponse = keeped[finalWinner]
        else:
            finalResponse = long(6)
        self.dbg("[FINALLY] {}".format(finalResponse),2)
        return self.readResponse(finalResponse)
        #return finalResponse

    def readResponse(self, response_id):
        self.dbg("<readResponse>")
        r = self.query.getResult(response_id).fetchone()
        return self.routeType(r)

    def routeType(self, result):
        self.dbg("<routeType>")
        scheme_r = self.query.db.t_response
        return self.showResponse(result[scheme_r.c.id])

    def showMessage(self, message):
        self.dbg("<showMessage>")
        print(str(message).decode('latin1'))

    def showResponse(self, command):
        self.dbg("<showResponse>")
        ci = self.query.getCommandInformations(command)
        d = dict(ci.fetchone())
        d["response"] = d["response"].decode('latin-1')
        res = (json.dumps(d))
        return res

    def applyCallback(self, cb_id):
        self.dbg("<applyCallback>")
        response = self.readResponse(cb_id)
        while response:
            response = self.readResponse(response)
        return response
    
    def __repr__(self):
        return "Je suis l'engine !!!"
