# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:13:15 2017

@author: Andrew
"""

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        def toStr(n,base):
           convertString = "0123456789ABCDEF"
           if n < base:
              return convertString[n]
           else:
              return toStr(n//base,base) + convertString[n%base]
        iBase3 = toStr(i,3)
        while len(iBase3) < N:
            iBase3 = "0" + iBase3
#        print(iBase3)
        for j in range(N):
            # test bit jth of integer i
#            print(j)
            if (int(iBase3[j])) == 1:
                bag1.append(items[j])
            if (int(iBase3[j])) == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

#n = 2        
#L= []
#        
#for i in range(n):
#    L += [i+1]
#
#test = yieldAllCombos(L)
#
#for i in range(3**n):
#    print(next(test))