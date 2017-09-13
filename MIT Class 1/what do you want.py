# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:12:42 2017

@author: Andrew
"""

# Write a program that counts up the number of vowels 
# contained in the string s. Valid vowels are: 
# 'a', 'e', 'i', 'o', and 'u'. For example, if 
# s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5



s = str(input("What do you want?")) 

vowel = 0
for letter in s:
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        vowel += 1
print("Number of vowels: " + str(vowel))