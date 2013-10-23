#!/bin/python
# -*- coding: utf-8 -*-
import sys, os, signal
from query.yengine import *
from context.ycontext import *
from debug.debug import *
from server.yserver import YServer

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

def manageServer(args, ctx):
    if "-s" in args:
        args.remove("-s")
        ctx.server = True
    if "-i" in args:
        args.remove("-i")
        ctx.interactive = True
    return args, ctx

# test de la fonction table
if __name__ == "__main__":
    ctx = YContext()
    sys.argv, ctx = manageVerbosity(sys.argv, ctx)
    sys.argv, ctx = managePlatform(sys.argv, ctx)
    sys.argv, ctx = manageServer(sys.argv, ctx)
    q = YEngine(sys.argv, ctx)
    if ctx.server:
        server = YServer(q, 1993)
        server.start()
    elif ctx.interactive:
        while not q.isTheEnd():
            question = raw_input("Y> ")
            q.changeQuery(question)
            print q.digest()
    else:
        print q.digest()
