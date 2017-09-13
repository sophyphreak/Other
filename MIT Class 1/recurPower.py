# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:09:00 2017

@author: Andrew
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if (exp == 0):
        return 1
    else:
        return base * recurPower(base, exp-1) 
        
print (recurPower(3,3))