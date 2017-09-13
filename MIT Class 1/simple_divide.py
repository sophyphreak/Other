# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:17:10 2017

@author: Andrew
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
      
       item / denom
       
   except ZeroDivisionError:
       
       return 0
       
   else:
       
       return item / denom