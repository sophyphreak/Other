# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:14:43 2017

@author: Andrew
"""

def fact(n):
    ans = 1
    for i in range(n):
        ans *= (i + 1)
    return ans

def pi(n):
    ans = 0
    for i in range(n+1):
        ans += (fact(6*n))*(545140134*n + 13591409)/((fact(3*n))*((fact(n))**3)*(-262537412640768000)**n)
    ans /= (426880*(10005)*.5)
    return ans**-1

