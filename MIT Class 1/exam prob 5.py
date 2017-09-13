# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 03:58:57 2017

@author: Andrew
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def stuff(x):
        answer = 0
        k = len(L)
        for i in range(k):
            answer += L[i] * x**(k-i-1)
        return answer
    return stuff