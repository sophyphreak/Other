# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:35:46 2017

@author: Andrew
"""

s = str(input("Please enter your text to be decoded:"))

alpha = "abcdefghijklmnopqrstuvwxyzabc"

#count = 0

alp1 = 0

begin = 0
end = 0

secretmessage = ""

for letter in range(0, len(s)):
#    if (len(s) - count < 2):
#        break
    for alp1 in range(0, 27):
        if (s[letter] == alpha[alp1]):
            secretmessage += alpha[alp1 + 2]
            break
        if alp1 == 26:
            secretmessage += s[letter]

print("")
print("And here is your secret message:")
print("")
print(secretmessage)

        
        
        
        
        