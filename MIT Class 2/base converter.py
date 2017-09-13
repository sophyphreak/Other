# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:35:47 2017

@author: Andrew
"""

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(26,3))