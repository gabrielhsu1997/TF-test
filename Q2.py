# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:27:20 2021

@author: Gabriel
"""

# I've tried this function but it doesn't work. 
# NameError springs up at function call itself and I don't really know to allow for parameters that are undefined variables.
def exists(*args):
    for arg in args:
        try:
            arg
        except NameError:
            print(str(arg)+"is not defined.")
        else:
            print(str(arg)+" is defined.")