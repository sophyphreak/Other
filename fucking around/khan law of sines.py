# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 03:19:38 2017

@author: Andrew
"""

import math


def toRad(num):
    return num/180*math.pi
    
def toDeg(num):
    return num/math.pi*180

print("I will help you find angle B")
A = float(input("angle A="))
a = float(input("side a="))
b = float(input("side b="))


ans = (math.asin(b*(math.sin(toRad(A))/a)))

ans = toDeg(ans)

print(ans)