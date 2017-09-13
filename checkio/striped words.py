# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 02:27:48 2017

@author: Andrew
"""

def checkio(text):
    vowels = "aeiouyAEIOUY"
    consonants = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"
    
    answer = 0
    
    def checkStriped(word):
        #input: string of letters
        #function increases answer if word is striped
        #returns nothing
        if word[0] in vowels:
            last = "v"
        else: 
            last = "c"
        striped = True
        
        for i in range(1, len(word)):
#            print("i=",i,"  word:", word, "   word[i]:", word[i], "   last:", last)
            if last == "v":
                if word[i] in vowels:
                    striped = False
#                    print(i)
                else:
                    last = "c"
            elif last == "c":
                if word[i] in consonants:
                    striped = False
#                    print(word[i])
                else:
                    last = "v"
        if striped == True:
            return 1
        else:
            return 0
        
    def findNextWord(text):
        #input: remaining text
        #returns: next word and remaining text
        word = "word"
        j = 0
        for i in range(len(text)):    
            if (text[i] in letters) or (text[i] in numbers):
                if text[i] in numbers:
                    word = "not word"
                j = i
                while (text[j] in letters or text[j] in numbers):
                    j += 1
                    if j >= len(text):
                        break
                    if text[j] in numbers:
                        word = "not word"
                break
        if j == 0:
            return 0
        if word == "not word":
            return ("a", text[j:])
        return (text[i:j],text[j:])
    
    while len(text) > 0:
        A = findNextWord(text)
#        print(A)
        if A == 0:
            return answer
        word = A[0]
        text = A[1]
        if len(word) > 1:
            answer += checkStriped(word)

    return answer

print(checkio("1st 2a ab3er root rate"))
            
##These "asserts" using only for self-checking and not necessary for auto-testing
#if __name__ == '__main__':
#    assert checkio("My name is ...") == 3, "All words are striped"
#    assert checkio("Hello world") == 0, "No one"
#    assert checkio("A quantity of striped words.") == 1, "Only of"
#    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
            