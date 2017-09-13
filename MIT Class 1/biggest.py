# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:48:46 2017

@author: Andrew
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    a = 0
    
    for i in aDict:
        if a < len(aDict[i]):
            a = len(aDict[i])
            b = i
    return b

            
    
    
    
#    list1 = []
#    for i in aDict:
#        list1.append(aDict[i])
#    list2 = []
#    for i in range(len(list1)):
#        list2.append(len(list1[i]))
#    return max(list2)
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print(biggest(animals))
