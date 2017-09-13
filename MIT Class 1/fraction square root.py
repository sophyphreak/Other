# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 05:31:07 2017

@author: Andrew
"""

x = .5
epsilon = .0000001
numGuesses = 0
low = 0
high = 1
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to square root of ' + str (x))
    