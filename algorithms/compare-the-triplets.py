#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a, b = 0, 0 
for ai, bi in zip((a0,a1,a2), (b0,b1,b2)): 
	if (ai > bi): a += 1 
	if (bi > ai): b+= 1
print (a, b)