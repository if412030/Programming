#!/usr/bin/env python

import sys


N = int(raw_input().strip())

if (N % 2 != 0):
    print "Weird"
if (N % 2 == 0 ) and (N >= 2 and N <=5):
    print "Not Weird"
if (N % 2 == 0 ) and (N >= 6 and N <=20):
    print "Weird"
if (N % 2 == 0 ) and (N > 20):
    print "Not Weird"
