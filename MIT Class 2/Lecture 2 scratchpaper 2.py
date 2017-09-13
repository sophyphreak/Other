# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 06:47:46 2017

@author: Andrew
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#L1 = [1,2,3,4]
#        
#a =  powerSet(L1)
#for i in range(2**len(L1)):
#    print(next(a))

