#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


numpos, numneg, numzero = 0, 0, 0
for x in arr: 
	if x == 0: numzero+=1
	if x > 0: numpos+=1
	if x < 0: numneg+=1

print (numpos/n)
print (numneg/n)
print (numzero/n)
