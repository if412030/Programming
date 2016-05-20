#!/usr/bin/env python

import sys


N = int(raw_input().strip())

totl = 0
for i in range(10):
    totl = N * (i+1)
    print "%d x %d = %d" % (N, i+1, totl)