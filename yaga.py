#!/bin/python
# -*- coding: utf-8 -*-
import sys, os, signal
from query.yengine import *
from context.ycontext import *
from debug.debug import *

def manageVerbosity(args, ctx):
    if "-v" in args:
        args.remove("-v")
        ctx.verbose = 0
    return args, ctx

def managePlatform(args, ctx):
    if "-p" in args:
        pos = args.index("-p")
        platform = args[pos + 1]
        args.remove("-p")
        args.remove(platform)
        ctx.platform.append(platform)
    return args, ctx

# test de la fonction table
if __name__ == "__main__":
    ctx = YContext()
    sys.argv, ctx = manageVerbosity(sys.argv, ctx)
    sys.argv, ctx = managePlatform(sys.argv, ctx)
    q = YEngine(sys.argv, ctx)
    if "-i" in sys.argv:
        while not q.isTheEnd():
            question = raw_input("Y> ")
            q.changeQuery(question)
            q.digest()
    else:
        q.digest()