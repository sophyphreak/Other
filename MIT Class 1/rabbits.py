# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:42:05 2017

@author: Andrew
"""


def rabbits(a, b, time):
    if time == 1:
        return b
    else:
        c = a + b
        a = b
        b = c
        time -= 1
        return rabbits(a, b, time)

print(rabbits(1, 1, 12))