# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:14:40 2017

@author: Andrew
"""

def checkio(data):

    rn = ""
    data1 = data
    
    while data1 > 999:
        rn += "M"
        data1 -= 1000
    if data1 > 899:
        rn += "CM"
        data1 -= 900
    if data1 > 499:
        rn += "D"
        data1 -= 500
    if data1 > 399:
        rn += "CD"
        data1 -= 400
    while data1 > 99:
        rn += "C"
        data1 -= 100
    if data1 > 89:
        rn += "XC"
        data1 -= 90
    if data1 > 49:
        rn += "L"
        data1 -=50
    if data1 > 39:
        rn += "XL"
        data1 -= 40
    while data1 > 9:
        rn += "X"
        data1 -= 10
    if data1 > 8:
        rn += "IX"
        data1 -= 9
    if data1 > 4:
        rn += "V"
        data1 -= 5
    if data1 > 3:
        rn += "IV"
        data1 -= 4
    while data1 > 0:
        rn += "I"
        data1 -= 1
    
    return rn

print(checkio (6) == 
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'