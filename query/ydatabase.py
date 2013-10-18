# -*- coding: utf-8 -*-
from sqlalchemy import *



class YDatabase:
    """Classe représentant une bdd yaga"""
    def __init__(self):
        self._connect()
        self._loadDatabaseShema(self.engine)
        
    def _loadDatabaseShema(self, e):
        self.meta = MetaData()
        self.t_expression = Table('expression', self.meta, autoload=True, autoload_with=e)
        self.t_language = Table('language', self.meta, autoload=True, autoload_with=e)
        self.t_platform = Table('platform', self.meta, autoload=True, autoload_with=e)
        self.t_value = Table('value', self.meta, autoload=True, autoload_with=e)
        self.t_response = Table('response', self.meta, autoload=True, autoload_with=e)
        self.t_response_scheme = Table('response_scheme', self.meta, autoload=True, autoload_with=e)

    def _connect(self):
        self.engine = create_engine('mysql://yaga-user:4GTEfUQtrLZ4qLN4@localhost/yaga')
        self.connection = self.engine.connect()
        return self.connection
        
    def _disconnect(self):
        self.connection.close()
        
    def getExprRequest(self, args):
        wh = []
        for arg in args:
            wh.append(self.t_expression.c.name.ilike("%" + arg + "%"))
        o = wh.pop()
        r = select("*", use_labels=True).select_from(self.t_expression\
            .join(self.t_value))
        while len(wh):
            o = or_(o, wh.pop())
        r = r.where(o)
        return r

    def getSchemeRequest(self, args):
        wh = []
        for arg in args:
            wh.append(self.t_response_scheme.c.pattern.ilike("%"+ arg + "%"))
        r = select("*", use_labels=True).select_from(self.t_response_scheme)
        o = wh.pop()
        while len(wh):
            o = or_(o, wh.pop())
        r = r.where(o)
        return r

    def __repr__(self):
        ret = ""
        for c in self.t_expression.columns:
            ret = ret + "{},".format(c)
        return "Schema actuel : {}".format(ret)