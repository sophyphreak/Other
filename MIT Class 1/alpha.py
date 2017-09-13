# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 04:35:47 2017

@author: Andrew
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # I want it to start in the center of the string, 
    #    then scan to 50% to the left or right depending 
    #    on greater/less than. First, let's build a normal
    #    bisection search
    low = 0
    high = len(aStr)
    ans = int((low + high) / 2)
#    print(ans)
#    print(aStr)
    if len(aStr) < 1:
        return False
    if char == aStr[ans]:
        return True
    elif len(aStr) < 2:
        return False
    if char < aStr[ans]:
#        print("char < aStr[ans]")
        return isIn(char, aStr[0:ans])
    if char > aStr[ans]:
#        print("char > aStr[ans]")
        return isIn(char, aStr[ans:high])



print(isIn("y", "bcddehhhhjjjjmmmmmmmmmmmmmmqqqqvwxyz"))