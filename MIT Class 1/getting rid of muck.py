# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:09:15 2017

@author: Andrew
"""

s = str(input("give me your muck"))

alpha = "abcdefghijklmnopqrstuvwxyz"

s1 = ""

for i in range(len(s)):

    for n in range(len(alpha)):
        
        if (s[i] == alpha[n]):
            s1 = s1 + s[i]

    
    
#    if (
#    s[i] != "!" and s[i] != "@" and s[i] != "#" and
#    s[i] != "$" and s[i] != "%" and s[i] != "^" and 
#    s[i] != "&" and s[i] != "*" and s[i] != "(" and
#    s[i] != ")" and s[i] != "_" and s[i] != "-" and
#    s[i] != "=" and s[i] != "+" and s[i] != "[" and
#    s[i] != "]" and s[i] != "{" and s[i] != "}" and
#    s[i] != ";" and s[i] != ":" and s[i] != " "
#    ):
#        s1 = s1 + s[i]

#print (s1)