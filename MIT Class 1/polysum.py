# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 05:40:58 2017

@author: Andrew
"""

import math

def polysum(n, s):
    '''
    input positive integers n and s
    n represents the number of sides of a normal polygon
    s represents the length of each side of that polygon
    
    returns the area of the polygon plus the perimeter squared
    '''
    area = (.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter = s * n
    perSq = perimeter**2
    
    return (round(area + perSq, 4))