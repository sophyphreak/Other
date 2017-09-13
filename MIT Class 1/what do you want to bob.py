# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:12:42 2017

@author: Andrew
"""


s = str(input("What do you to alphabet?")) 

count = 0
bobs = 0
for letter in s:
    if (len(s) - count < 3):
        break
    if (s[count] + s[count + 1] + s[count + 2] == "bob"):
        bobs += 1
    count += 1
        
print("Number of times bob occurs is: " + str(bobs))