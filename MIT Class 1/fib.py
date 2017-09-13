# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:53:15 2017

@author: Andrew
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib (x-1) + fib(x-2)