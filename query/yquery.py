# -*- coding: utf-8 -*-
from ydatabase import *
from sqlalchemy import *
from debug.debug import *
from base.ybase import *


class YQuery(YBase):
    """Classe représentant une requete yaga"""
    def __init__(self, query, ctx):
        """Constructeur de notre classe"""
        YBase.__init__(self, ctx)
        self.dbg("  <newquery> : {} ({})".format(query, type(query)), 2)
        self.dbg("  <ctx> : {} ({})".format(self.ctx, type(self.ctx)), 2)
        self.query = self.cleanQuery(query)
        self.db = YDatabase(ctx)

    def cleanQuery(self, query):
        if not (self.ctx.interactive or self.ctx.server) and (len(query) > 1):
            query = query[1:]
            return " ".join(query)
        else:
            return query

    def searchEntireExpression(self):
        return self.searchExpression(self.query)

    def searchExpression(self, e):
        request = self.db.getExprRequest([e])
        result = self.db.connection.execute(request)
        self.dbg("resultats de la requete [{}]: {}".format(request, result))
        return result

    def searchArrayExpression(self, e):
        request = self.db.getExprRequest(e)
        result = self.db.connection.execute(request)
        self.dbg("resultats de la requete [{}]: {}".format(request, result))
        return result

    def searchMatches(self, value):
        request = self.db.getSchemeRequest(value)
        result = self.db.connection.execute(request)
        self.dbg("resultats de la requete [{}]: {}".format(request, result))
        return result

    def getResult(self, result_id):
        request = self.db.getResultRequest(result_id)
        result = self.db.connection.execute(request)
        self.dbg("[GR] resultats de la requete [{}]: {}".format(request, result),3)
        return result

    def getCommandInformations(self, result_id):
        request = self.db.getCommandInformations(result_id)
        result = self.db.connection.execute(request)
        self.dbg("[CI] resultats de la requete [{}]: {}".format(request, result),3)
        return result

    def __repr__(self):
        return "Requete actuelle: {} ({})".format(
                self.query, self.db)
