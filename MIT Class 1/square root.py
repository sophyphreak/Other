# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 04:03:21 2017

@author: Andrew
"""

ans = 0
neg_flag = False
x = float(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 != x:
    ans -= 1
    while ans**2 < x:
       ans = ans + .1

if ans**2 != x:
    ans -= .1
    while ans**2 < x:
        ans = ans + .01

if ans**2 != x:
    ans -= .01
    while ans**2 < x:
        ans = ans + .001
        
if ans**2 != x:
    ans -= .001
    while ans**2 < x:
        ans = ans + .0001
        
if ans**2 != x:
    ans -= .0001
    while ans**2 < x:
        ans = ans + .00001
        
if ans**2 != x:
    ans -= .00001
    while ans**2 < x:
        ans = ans + .000001

if ans**2 != x:
    ans -= .000001
    while ans**2 < x:
        ans = ans + .0000001        
        
if ans**2 >= x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")