#!/bin/python3

import sys


# n = int(input().strip())
n = 6

def makeStairs(n): 
	a = [[' ']*n]*n
	x = 0
	while (x < n): 
		v = x + 1
		s = n - v 
		c = n - 1 

		while (s <= c): 
			a[x][s] = '#'
			s+=1
		x+=1 

	
		
	print (a)
	return (a)

for x in makeStairs(n): 
	print ("".join(x))