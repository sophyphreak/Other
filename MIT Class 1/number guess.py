# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 05:35:02 2017

@author: Andrew
"""
print("Please think of a number between 0 and 100!")
low = 0
high = 100


player = "0"

while player != "c":
    ans = int((low + high) / 2)
    print ('Is your secret number ' + str(ans) + "?")
    
    player = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if player == "c":
        break
    elif player == "h":
        high = ans
    elif player == "l":
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    
print("Game over. Your secret number was: " + str(ans))