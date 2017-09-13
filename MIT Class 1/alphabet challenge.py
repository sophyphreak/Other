# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:15:27 2017

@author: Andrew
"""

s = "zyxwvutsrqponmlkjihgfedcba" 

if (len(s) != 1):

    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    count = 0
    
    alp1 = 0
    alp2 = 0
    
    begin = 0
    end = 0
    
    ans = "-"
    
    for letter in range(len(s)-1):
        if (len(s) - count < 2):
            break
        for alp1 in range(26):
            if (s[letter] == alpha [alp1]):
                break
        for alp2 in range(26):
            if (s[letter + 1] == alpha [alp2]):
                break
        if (alp1 <= alp2):
            ans = ans + "1"
        else:
            ans = ans + "0"
    
    #print (ans)
    
    longest = 0
    
    longestdigit = 0
    
    for digit in range(1, len(ans)-1):
    # for everything here we need to find out if the current
    # digit is a 1 and then find out if the next digit is a 1
    
        templong = 0
    
    # We will do this using templong. templong will be the 
    # length of our current row of 1's, and that will be compared
    # to our longest row of 1's later to determine the longest
    # row of places in alphabetical order
        
        for num in range(digit, len(ans)):
            if (ans[num] == "1"):
                templong += 1
            if (ans[num] == "0"):
                break
        if (templong > longest):
            longest = templong
            longestdigit = digit
    
#    print ("longest: " + str(longest))
#    print ("longestdigit: " + str(longestdigit))        
#    print (type(longest))
#    print (type(longestdigit))
    if (longest == 0 and longestdigit == 0):
        longestdigit = 1
        
        
    answerstring = ""
    
    for i in range(longestdigit - 1, longestdigit + longest):
        answerstring += s[i]

    if answerstring == "":
        answerstring = s[0]
    
    # print (s[longestdigit-1])
    # print ("Longest substring in alphabetical order is: " + answerstring)
    print ("Longest substring in alphabetical order is: " + s[longestdigit - 1: longestdigit + longest])

else:
    print ("Longest substring in alphabetical order is: " + s[0])


    
    