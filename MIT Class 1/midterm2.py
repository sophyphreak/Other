# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 03:30:56 2017

@author: Andrew

For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) 
    mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L) 
print(L)

"""

 

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L.
    
    It does not return anything.
    """
    for i in range(int(len(L) / 2)):
        L[i] , L[len(L) - 1 - i] = L[len(L) - 1 - i], L[i]
    for i in L:
        for j in range(int(len(i) / 2)):
            i[j] , i[len(i) - 1 - j] = i[len(i) - 1 - j], i[j]