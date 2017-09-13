# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 04:38:54 2017

@author: Andrew

Write a function to flatten a list. The list contains other lists, strings, or 
    ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into 
    [1,'a','cat',2,3,'dog',4,5] (order matters).

Recursion is extremely useful for this question. You will have to try to 
flatten every element of the original list. To check whether an element can be 
flattened, the element must be another object of type list.

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])

"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    bList = []
    
    def flatten_helper(x):
    
        if type(x) == list:
            for i in range(len(x)):
                return [] + [flatten_helper(x[i])]
        else:
            return x
    
    for x in aList:
        bList += [flatten_helper(x)]
    
    return bList