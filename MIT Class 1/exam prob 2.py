# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 01:59:06 2017

@author: Andrew
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    #first, check longest monotonically increasing numbers
    #And then mark the value at which this starts as well as the length of string
    incLen = 0
    incLoc = 0
    
    for i in range(len(L) - 1):
#        print("i EQUALS", i)
        j = i + 1
        while L[j] >= L[j - 1]:
            j += 1
            if j - i > incLen:
                incLen = j - i
                incLoc = i
            if j >= len(L):
                break
#    test = []
#    for i in range(incLen):
#        test += [L[incLoc + i]]
#    return test

    #then check for monotonically decreasing
    decLen = 0
    decLoc = 0
    
    for i in range(len(L) - 1):
#        print("i EQUALS", i)
        j = i + 1
        while L[j] <= L[j - 1]:
            j += 1
#            print("j EQUALS", j)
            if j - i > decLen:
                decLen = j - i
                decLoc = i
            if j >= len(L):
                break
#    test = []
#    for i in range(decLen):
#        test += [L[decLoc + i]]
#    return test
    #then compare the two for length. Tiebreaker is location
    winner = ""
    
    if decLen > incLen:
        winner = "dec"
    elif decLen < incLen:
        winner = "inc"
    elif decLen == incLen:
        if decLoc < incLoc:
            winner = "dec"
        else:
            winner = "inc"
    
    #sum and return
    ansList = []
    if winner == "dec":
        for i in range(decLen):
            ansList += [L[decLoc+i]]
    elif winner == "inc":
        for i in range(incLen):
            ansList += [L[incLoc+i]]
    finalAns = 0
    for i in ansList:
        finalAns += i
#    print(winner)
#    print(ansList)
    return finalAns
    
    
L = [100, 200, 300, -100, -200, -1500, -5000]
print(longest_run(L))
        