# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 03:35:11 2017

@author: Andrew
"""
import math


def toRad(num):
    return num/180*math.pi
    
def toDeg(num):
    return num/math.pi*180
        
def findSide():
    print("I will help you find side c")
    a = float(input("side a="))
    b = float(input("side b="))
    C = float(input("angle C="))
    
    #c squared = a squared + b squared -2ab*cos(C)
    
    ans = a**2 + b**2 - 2*a*b*math.cos(toRad(C))
    
    ans = math.sqrt(ans)

    print("c=",ans)

def findAngle():
    print("I will help you find angle C")
    a = float(input("side a="))
    b = float(input("side b="))   
    c = float(input("side c="))
    
    #arccos(c squared - a squared - b squared)/-2ab)
    C = toDeg(math.acos((c**2 - a**2 - b**2)/(-2*a*b)))
    
    print("C=", C)

flag = 0

while flag == 0:
    print("Do you want to find a side or an angle?")
    begin = input("s for side, a for angle: ")
    if begin == "s":
        findSide()
        flag = 1
    elif begin == "a":
        findAngle()
        flag = 1
    else:
        print("Sorry, not a valid input. Please try again.")