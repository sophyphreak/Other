# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:20:58 2017

@author: Andrew
"""

x = str(input("enter a lower-case letter please: "))

a = "abcdefghijklmnopqrstuvwxyz"

x = x[0]

for i in range(len(a)):
    if (x == a[i]):
        print ("That is letter number", len(a[0:i]) + 1, "in the alphabet")
        break
