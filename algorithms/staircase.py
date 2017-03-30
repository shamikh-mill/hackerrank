#!/bin/python3

import sys


# n = int(input().strip())
n = 4

def makeStairs(n): 
	a = [[' ']*n]*n
	v = n - 1 
	while (v > 0): 
		i = 0 
		a[i][v] = '#'
		i+=1
		v-=1

	return (a)

for x in makeStairs(n): 
	print ("".join(x))