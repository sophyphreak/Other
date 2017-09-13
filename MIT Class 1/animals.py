# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:25:38 2017

@author: Andrew
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    list2 = []
    for i in aDict:
        for g in range(len(aDict[i])):
            list2.append(aDict[i][g])
    many = 0
    for i in list2:
        many += 1
    return many
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))