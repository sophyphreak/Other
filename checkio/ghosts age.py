# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:13:01 2017

@author: Andrew
"""

def checkio(num):
    fib = [0,1]
    while True:
        fib += [fib[len(fib)-1] + fib[len(fib)-2]]
        if fib[-1] > 10000:
            break
    ghost = []
    base = 10000
    for i in range(5000):
        if i in fib:
            base -= i
            ghost += [base]
        else:
            base += 1
            ghost += [base]
#    print(ghost)
    for i in range(5000):
        if ghost[i] == num:
            return i
print(checkio(9990))