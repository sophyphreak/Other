# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:24:43 2017

@author: Andrew
"""

class Bracket():
    '''
    input: a string. Either "{", "[", or "("
    '''
    def __init__(self, start):
        self.start = start
        if self.start == "{":
            self.end = "}"
        elif self.start == "[":
            self.end = "]"
        else:
            self.end = ")"
    
    def checkEnd(self, end):
        if not end == self.end:
            return False
        else:
            return True
        
def checkio(string):
    '''
    input: string
    returns True or False. True if brackets are ok, False otherwise
    '''
    bracketList = []
    for char in string:
        if char in "{[(":
            bracketList += [Bracket(char)]
        if char in "}])":
            if bracketList == []:
                return False
            if not bracketList[-1].checkEnd(char):
                return False
            del bracketList[-1]
    if not bracketList == []:
        return False
    return True
            
            
            
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

            
            
            
            
            