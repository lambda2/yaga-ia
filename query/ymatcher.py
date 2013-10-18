# -*- coding: utf-8 -*-
from debug.debug import *
from base.ybase import *


class YMatcher(YBase):
    """Classe représentant une bdd yaga"""
    def __init__(self, dist_scheme, current_scheme, ctx):
        YBase.__init__(self, ctx)
        self.dist = dist_scheme
        self.current = current_scheme
        self.results = dict()
    
    def computeSchemes(self):
        for e in self.dist:
            self.results[e] = self.getComputeScore(e)
        self.dbg("Computing ended !")
        self.dbg("[SCORES] {}".format(self.results),1)
        self.dbg("[WIN] {}".format(max(self.results)),3)
        max_ = max(self.results)
        return {max_:self.results[max_]}
        
    def getComputeScore(self, scheme):
        if type(scheme) == str:
            scheme = scheme.split(" ")
        """
        experiments
        """

        """
        end expermiments
        """
        input_count = len(self.current)
        dist_count  = len(scheme)
        matchers = 0
        for elt in self.current:
            if elt in scheme:
                matchers = matchers + 1
        self. dbg("[#] [Matchers->{}]\t[i_count->{}]\t[dist_count->{}]".format(
            matchers, input_count, dist_count))
        mult = float(input_count) / float(dist_count)
        score = float(float(matchers * 100)/float(dist_count * 100))  * 100 / mult
        self.dbg("{} | {} \n >>\t{}%".format(" ".join(self.current)," ".join(scheme),score))
        return score

    def __repr__(self):
        ret = ""
        for c in self.t_expression.columns:
            ret = ret + "{},".format(c)
        return "Schema actuel : {}".format(ret)