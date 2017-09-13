# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 07:42:53 2017

@author: Andrew
"""
import math

def toRad(num):
    return num/180*math.pi
    
def toDeg(num):
    return num/math.pi*180

pi = math.pi
a = math.asin(-1)*(1/18)
a1 =  pi- a

for i in range(5):
    print((a + 2*pi*i))
    print((a1 + 2*pi*i))