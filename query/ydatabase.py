# -*- coding: utf-8 -*-
from sqlalchemy import *
from base.ybase import *


class YDatabase(YBase):
    """Classe représentant une bdd yaga"""
    def __init__(self, ctx):
        YBase.__init__(self, ctx)
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
        self.t_response_type = Table('response_type', self.meta, autoload=True, autoload_with=e)
        self.t_module = Table('module', self.meta, autoload=True, autoload_with=e)
        self.t_module_requires = Table('module_requires', self.meta, autoload=True, autoload_with=e)
        

    def _connect(self):
        self.engine = create_engine('mysql://yaga-user:4GTEfUQtrLZ4qLN4@localhost/yaga', encoding='latin1')
        self.connection = self.engine.connect()
        return self.connection
        
    def _disconnect(self):
        self.connection.close()
        
    def getExprRequest(self, args):
        self.dbg("ARGS = : {} ({})".format(args, type(args)), 1)
        wh = []
        if type(args) == str:
            args = [args]
        self.dbg("Arguments de requete : {}".format(args), 1)
        for arg in args:
            wh.append(self.t_expression.c.name.ilike(arg))
        o = wh.pop()
        r = select("*", use_labels=True).select_from(self.t_expression\
            .join(self.t_value))
        while len(wh):
            o = or_(o, wh.pop())
        r = r.where(o)
        return r

    def getSchemeRequest(self, args):
        wh = []
        if type(args) == str:
            args = [args]
        for arg in args:
            wh.append(self.t_response_scheme.c.pattern.ilike("%"+ arg + "%"))
        r = select("*", use_labels=True).select_from(self.t_response_scheme)
        o = wh.pop()
        while len(wh):
            o = or_(o, wh.pop())
        r = r.where(o)
        return r

    def getResultRequest(self, args):
        wh_pl = []
        for platform in self.ctx.platform:
            wh_pl.append(self.t_platform.c.name == platform)
        r = select(
            [
                self.t_response.c.id,
                self.t_response.c.response,
                self.t_response.c.callback,
                self.t_response_type.c.type_name
            ],
            use_labels=True).select_from(self.t_response\
            .join(self.t_language)
            .join(self.t_platform)
            .join(self.t_response_type)
        )
        p = wh_pl.pop()
        while len(wh_pl):
            p = or_(p, wh_pl.pop())
        r = r.where(and_(
            self.t_response.c.id == args,
            p,
            self.t_language.c.abbr == self.ctx.lang))
        return r

    def getCommandInformations(self, id_):
        lg = self.t_language.alias()
        r = select(
            [
                self.t_response.c.id.label('id'),
                self.t_response.c.response.label('response'),
                self.t_response.c.callback.label('callback'),
                self.t_response_type.c.type_name.label('type'),
                self.t_module.c.module_name.label('module'),
                lg.c.abbr.label('lang'),
                self.t_platform.c.name.label('platform')
            ],
            use_labels=True).select_from(self.t_response\
            .join(lg)
            .join(self.t_platform)
            .join(self.t_response_type)
            .outerjoin(self.t_module)
        ).where(self.t_response.c.id == id_)
        return r

    def __repr__(self):
        ret = ""
        for c in self.t_expression.columns:
            ret = ret + "{},".format(c)
        return "Schema actuel : {}".format(ret)