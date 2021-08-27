# -*- coding: utf-8 -*-
import numpy as np

def pascaltri(n):
    if n > 0: # positive integer input
        newarr = np.zeros([n,n], dtype = int) # inititalise array
        newarr[0][0] = 1
        print(1)
    for i in range(1, n, 1): # iterate over each row
        newarr[i][0] = 1 # update first column
        print(1, end = ' ')
        for j in range(1, i+1, 1):
            newarr[i][j] = newarr[i-1][j-1]+newarr[i-1][j] # for each entry, sum the entry above and to the left
            print(newarr[i][j], end = ' ')
        print('')