#!/usr/bin/env python# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

for i in range(N):
	s = raw_input()
	res="";
	for idx in range(len(s)):
		if (idx % 2 == 0):
			res+= s[idx]
	res+=' '
	for idx in range(len(s)):
		if (idx % 2 == 1):
			res+= s[idx]
	print res