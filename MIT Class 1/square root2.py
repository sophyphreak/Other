# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 04:57:33 2017

@author: Andrew
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(guess)
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))