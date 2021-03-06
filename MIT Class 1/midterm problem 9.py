# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 06:03:42 2017

@author: Andrew

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])

"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    bList = []
    if type(aList) == list:
        for i in aList:
            bList += flatten(i)
        return bList
    else:
        bList += [aList]
        return bList
            
