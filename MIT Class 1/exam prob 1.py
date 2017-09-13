# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 01:44:05 2017

@author: Andrew
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if len(us_num) == 1:
        return trans[us_num]
    if us_num[0] == "1":
        answer = "shi"
        if us_num[1] != '0':
            answer += " " + trans[us_num[1]]
        return answer
    else:
        answer = ""
        answer += trans[us_num[0]] + " shi"
        if us_num[1] != '0':
            answer += " " + trans[us_num[1]]
        return answer


print(convert_to_mandarin('15')) #will return shi liu