#!/usr/bin/env python

# Enter your code here. Read input from STDIN. Print output to STDOUT
meal = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

v_tip = meal * tipPercent/100
v_tax = meal * taxPercent/100
t_cost = meal + v_tip + v_tax

print 'The total meal cost is %d dollars.' % round(t_cost)
