# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:27:04 2017

@author: Andrew
"""

x = str(input("Enter two lower case letters please: "))

a = "abcdefghijklmnopqrstuvwxyz"

x = x[0:2]

for i in range(len(a)):
    if (x[0] == a[i]):
        letter1 = len(a[0:i]) + 1
                      
for i in range(len(a)):
    if (x[1] == a[i]):
        letter2 = len(a[0:i]) + 1
                      
print ("They are", abs(letter2 - letter1), "letters away from one another")