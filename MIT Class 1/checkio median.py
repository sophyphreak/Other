# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:55:39 2017

@author: Andrew
"""

def checkio(data):

    data1 = sorted(data)
    if (len(data) % 2 == 0):
        i = int(len(data) / 2) - 1
        j = int(len(data) / 2)
        median = (data1[i] + data1[j]) / 2
    if (len(data) % 2 == 1):
        i = int(len(data) / 2)
        median = data1[i]
    return median

data = [1, 2, 3, 1000]    

print(checkio(data))