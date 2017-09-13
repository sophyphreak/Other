# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:04:04 2017

@author: Andrew
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    prod =1
    
    for i in range(exp):
        prod *= base
    
    return prod
    
print( iterPower(3,3) )