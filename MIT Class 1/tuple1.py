# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 06:10:58 2017

@author: Andrew
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    for t in range(len(aTup)):
        if t % 2 == 0:
            bTup = bTup + aTup[t:t+1]
            
    return bTup
    
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))