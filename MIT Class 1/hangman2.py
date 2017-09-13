# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:41:15 2017

@author: Andrew
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord1 = []
    secretWord = list(secretWord)
    secretWord1 = secretWord1 + secretWord
    for i in range(len(secretWord1)):
        secretWord1[i] = [secretWord1[i], False]
    for i in range(len(secretWord)):
        for j in lettersGuessed:
            if secretWord[i] == j:
                secretWord1[i] = [secretWord[i], True]
    for i in range(len(secretWord)):
        if (secretWord1[i] == [secretWord[i], False]):
            return False
    return True
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord1 = []
    display = ""
    secretWord = list(secretWord)
    secretWord1 = secretWord1 + secretWord
    for i in range(len(secretWord1)):
        secretWord1[i] = [secretWord1[i], False]
    for i in range(len(secretWord)):
        for j in lettersGuessed:
            if secretWord[i] == j:
                secretWord1[i] = [secretWord[i], True]
    for i in range(len(secretWord)):
        if (secretWord1[i] == [secretWord[i], True]):
            display = display + secretWord[i] + " "
        else:
            display = display + "_" + " "
    return display



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    display = ""
    for i in alphabet:
        if not i in lettersGuessed:
            display = display + i
    return display
                
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
#    availableLetters = getAvailableLetters(lettersGuessed)
    dashes = "-----------"
    guessesLeft = 8
    lettersFrequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 
                        'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 
                        'j', 'x', 'q', 'z']
    freq = 0
    print('Welcome to the game Hangman!')
    print("I'm thinking of a word that is", len(secretWord), "letters long.")
    print(dashes)
    iterations = 0
    guessesLeft = 1
    lettersGuessed = lettersFrequency
    while (isWordGuessed(secretWord, lettersGuessed)) == False:
        iterations += 1
        print('This is guess number', iterations)
        print('Available letters:', getAvailableLetters(lettersGuessed))
        print(freq)
        guess = lettersGuessed[freq]
        freq += 1
        if(guess in lettersGuessed):    
            print("Oops! You've already guessed that letter:", 
                  getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += [guess]
            if not guess in secretWord:
                print('Oops! That letter is not in my word: ', 
                      getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
            else:
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            print(dashes)
    

    
    if guessesLeft == 0:
        print('Sorry, you ran out of guesses. The word was ' 
              + secretWord + '.')
        return iterations
    else:
        print('Congratulations, you won!')
        return iterations




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#print(hangman(secretWord))

def findWinRatio(iterations):
    '''
    iterations: int, number of you want to run to find the win ratio for
    a hangman win method
    
    returns: ratio of wins to losses of the hangman method used
    '''
    numberOfIterations = 0
    
    list1 = []

    itr = 0

    while itr < iterations:
        list1 += [hangman(chooseWord(wordlist).lower())]
        numberOfIterations += 1
        itr += 1
    
    x = 0
    
    for i in list1:
        x += list1[i]
    average = x / len(list1)
    print("Number of Iterations:", numberOfIterations)
    return average
    
print(findWinRatio(10))


        
    
