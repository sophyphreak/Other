# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 00:24:47 2017

@author: Andrew
"""

def gcdRecur(a, b):
    
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a % b)

print (gcdRecur(100, 40))