# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 03:28:49 2017

@author: Andrew
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList
print(aList is bList)