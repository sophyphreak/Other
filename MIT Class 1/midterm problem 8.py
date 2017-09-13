# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 02:31:15 2017

@author: Andrew

For example, the following functions, f, g, and test code:

    def f(i):
        return i + 2
    def g(i):
        return i > 5

    L = [0, -10, 5, 6, -4]
    print(applyF_filterG(L, f, g))
    print(L)

Should print:

    6
    [5, 6]

For this question, you will not be able to see the test cases we run. This 
    problem will test your ability to come up with your own test cases.


"""
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    i = 0
    
    while i < len(L):
        if g(f(L[i])) == False:
            del L[i]
        else: 
            i += 1
    
    if L == []:
        return -1
    else:
        return max(L)
            
        
                
        