# -*- coding: utf-8 -*-

def unique(liste):
    o_list = []
    for elt in liste:
        if type(elt) == list:
            elt = unique(elt)
        try:
            ind = o_list.index(elt)
        except:
            o_list.append(elt)
    return o_list