# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:20:47 2017

@author: Andrew
"""

def safe_pawns(pawns):
    pawnList = list(pawns)
    board = []
    for i in range(8):
        board += [[]]
    for i in range(8):
        for j in range(8):
            board[i] += [[" "]]
    def convLetter(letter):
        #converts letter to list place
        letStr = "abcdefgh"
        for i in range(8):
            if letStr[i] == letter:
                return i
    def convNumber(number):
        #converts number into list place
        numStr = "87654321"
        for i in range(8):
            if numStr[i] == number:
                return i
    #construct pawn tuple list
    pawnTuple = []
    for pawn in pawnList:
        pawnTuple += [(convLetter(pawn[0]),convNumber(pawn[1]))]
    
#    print(pawnTuple)
    
    #put pawns on board
    for pawn in pawnTuple:
        board[pawn[1]][pawn[0]] = ["p"] 
    
    safePawns = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == ["p"]:
                if not i == 7:
                    if not j == 0 and not j == 7:
                        if board[i+1][j+1] == ["p"] or board[i+1][j-1] == ["p"]:
                            safePawns += 1    
                    if j == 7:
                        if board[i+1][j-1] == ["p"]:
                            safePawns += 1
                    if j == 0:
                        if board[i+1][j+1] == ["p"]:
                            safePawns += 1
#    for i in board:
#        print (i)
    return safePawns
    
    
print(safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]))