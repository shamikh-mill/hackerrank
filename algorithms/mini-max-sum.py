#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
l = a,b,c,d,e 

a = []
for x in range(len(l)): 
	t = sum([l[y] for y in range(len(l)) if y != x])
	a.append(t)


print (min(a), max(a))




