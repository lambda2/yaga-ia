# -*- coding: utf-8 -*-
import sys, os, signal
from query.yquery import *

# test de la fonction table
if __name__ == "__main__":
    print("Argument : {}".format(sys.argv))
    q = YQuery(sys.argv)
    print(q)
    q.searchEntireExpression()