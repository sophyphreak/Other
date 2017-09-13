# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 01:20:15 2017

@author: Andrew
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    exp = 0
        
    if num == 1:
        return 0
    
    while base**exp < num:
        exp += 1
    
    diff1 = abs(base**(exp - 1) - num)
    diff2 = abs(base**(exp) - num) 
    
    if diff1 > diff2:
        return exp
    else: 
        return exp - 1
    
    