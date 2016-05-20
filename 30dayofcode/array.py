#!/usr/bin/env python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))[::-1]

print " ".join(map(str, arr))