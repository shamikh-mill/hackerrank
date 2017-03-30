#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)


diag1_sum = 0
for i in range(n):
	for j in range(n): 
		if i == j: diag1_sum += a[i][j]

diag2_sum = 0
for i in range(n): 
	diag2_sum += a[n - 1 - i][i]

print (abs(diag2_sum - diag1_sum))






    # for second diagonal, start at bottom left and take 1 from row and add one to column each time 


    
