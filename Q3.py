# -*- coding: utf-8 -*-
import numpy as np


def pascaltri(n):
    if n > 0:
        newarr = np.zeros([n,n], dtype = int)
        newarr[0][0] = 1
        print(1)
    for i in range(1, n, 1):
        newarr[i][0] = 1
        print(1, end = ' ')
        for j in range(1, i+1, 1):
            newarr[i][j] = newarr[i-1][j-1]+newarr[i-1][j]
            print(newarr[i][j], end = ' ')
        print('')