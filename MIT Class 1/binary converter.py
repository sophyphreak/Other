# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 05:58:02 2017

@author: Andrew
"""

num = .375

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if isNeg:
    result = "-" + result
    
print(result)