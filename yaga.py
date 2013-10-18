# -*- coding: utf-8 -*-
import sys, os, signal
from query.yengine import *
from debug.debug import *

# test de la fonction table
if __name__ == "__main__":
    dbg("Argument : {}".format(sys.argv))
    q = YEngine(sys.argv)
    if "-v" in sys.argv:
        gdebug = True
    if "-i" in sys.argv:
        while not q.isTheEnd():
            question = raw_input("Y> ")
            q.changeQuery(question)
            q.digest()
    else:
        q.digest()