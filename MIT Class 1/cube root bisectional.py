# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 05:26:38 2017

@author: Andrew
"""

x = 54
epsilon = .01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to cube root of ' + str (x))
    