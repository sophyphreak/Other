# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:58:56 2017

@author: Andrew
"""

def palin(x):
    
    
    if len(x) == 1 or len (x) == 0:
        return True
    elif x[0] == x[len(x)-1]:
        return palin(x[2:len(x)-2])
    else:
        return False
        
print(palin("ablewasiereisawelba"))