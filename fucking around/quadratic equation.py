# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:03:24 2017

@author: Andrew
"""

def findX(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    
    x = []
    if 0 > (b**2 - 4*a*c):
        return "No x's"
    else:
        x += [(-b-(b**2-4*a*c)**.5)/(2*a)]
        x += [(-b+(b**2-4*a*c)**.5)/(2*a)]
        if x[0] == x[1]:
            x = [x[0]]
    return x
    
a = input("a =")
b = input("b =")
c = input("c =")

print("x =", findX(a,b,c))