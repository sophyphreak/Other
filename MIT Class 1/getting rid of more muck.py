# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:44:14 2017

@author: Andrew
"""

# view-source:http://www.pythonchallenge.com/pc/def/equality.html
# answer: linkedlist


alpha1 = "abcdefghijklmnopqrstuvwxyz"

alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ""

test = ""
weirdtest = ""

s = str(input("give me your muck"))

for i in range(len(s)):

    for i2 in range(len(alpha2)): #1st big letter on the left
        if (s[i] == alpha2[i2]):
            for i3 in range(len(alpha2)): #2nd big letter on the left
                if (s[i+1] == alpha2[i3]):
                    for i4 in range(len(alpha2)): #3rd big letter on the left
                        if (s[i+2] == alpha2[i4]):
                            for i5 in range(len(alpha1)): # target letter
                                if (s[i+3] == alpha1[i5]):
                                    for i6 in range(len(alpha2)): #1st big letter on the right
                                        if (s[i+4] == alpha2[i6]):
                                            for i7 in range(len(alpha2)): #2nd big letter on the right
                                                if (s[i+5] == alpha2[i7]):
                                                    for i8 in range(len(alpha2)): #3rd big letter on the right
                                                        if (s[i+6] == alpha2[i8]):  
                                                            test = test + s[i-1:i+8] + " "
                                                            weirdtest = weirdtest + s[i+3]
                                                            #problem begins here
                                                            
                                                            
                                                            
                                                            for i9 in range(len(alpha1)): #check to make sure there is a lower case letter on the left
                                                                if (s[i-1] == alpha1[i9]):
                                                                    for i10 in range(len(alpha1)): #check to make sure there is a lower case letter on the right
                                                                        if (s[i+7] == alpha1[i10]):
                                                                            answer = answer + s[i+3]
                                                                            
                                                                        
#            answer = answer + s[i]

# print (answer)