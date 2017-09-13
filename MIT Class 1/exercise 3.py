# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:23:48 2017

@author: Andrew
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
    
print(a(3>2, a, b))