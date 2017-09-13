# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 02:02:25 2017

@author: Andrew
"""

def checkio(maze_map):
    #input: maze in list form
    #returns: string with directions for an AI that can get through the maze
    
    #objective: move piece from spot [1][1] to [10][10]
    #If a bot leaves a spot, then it leaves a "2." If the bot is trapped and
    #has to move backwards, then it leaves a "3."
    
    answer = ""

    
    def testMove2(i,j):
        #input: integers with current location
        #output: valid move. Prefers E then S then W then N.
        #Always moves backwards.
        
        maze_map[i][j] = 3

        if maze_map[i][j+1] == 2:
            return "E"
        elif maze_map[i+1][j] == 2:
            return "S"
        elif maze_map[i][j-1] == 2:
            return "W"
        elif maze_map[i-1][j] == 2:
            return "N"
    
    def testMove1(i, j):
        #input: integers with current location
        #output: valid move. Prefers E then S then W then N.
        #Does not move backwards. If no move can fulfill these criteria, then
        #returns "X"
        #Also changes current space to "2"
                
        maze_map[i][j] = 2
        
        if maze_map[i][j+1] == 0:
            return "E"
        elif maze_map[i+1][j] == 0:
            return "S"
        elif maze_map[i][j-1] == 0:
            return "W"
        elif maze_map[i-1][j] == 0:
            return "N"
        else:
            return "X"
            
    def move(i, j, letter):
        #input: int i and j with current location; string letter with next move
        #returns: tuple (i,j) with new location after movement
        if letter == "E":
            j += 1
        if letter == "S":
            i += 1
        if letter == "W":
            j -= 1
        if letter == "N":
            i -= 1
        return (i,j)
    
    i = 1
    j = 1
        
    while not (i == 10 and j == 10):
        M = testMove1(i, j)
        if M == "X":
            M = testMove2(i, j)
        answer += M
        new = move(i, j, M)
        i = new[0]
        j = new[1]
    
#    for k in range(12):
#        print(maze_map[k])

    return answer

print(checkio( [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))