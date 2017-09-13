# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:57:23 2017

@author: Andrew
"""

def recall_password(cipher_grille, ciphered_password):
    #input: tuples--cipher grille and ciphered password
    #returns: string, decoded password
    
    #Create skeleton cipher grilles 2, 3, and 4
    
    def intoLoca(i,j):
        #input: list places
        #returns: all list places of other cipher grilles in a list
        
        #convert list places into a vector
        if j < 2:
            v = j-2
        else:
            v = j-1
        if i > 1:
            u = -i+1
        else:
            u = -i+2
        
        co1 = (v,u)
        co2 = (u,-v)
        co3 = (-v,-u)
        co4 = (-u,v)
        coAll = [co1, co2, co3, co4]
#        print(coAll)
        
        cipherSpots = []

        def returnCoor(x,y):
            #inputs: integers. value of x and y to convert back into i and j
            
            #returns: a tuple containing the i and j coordinates 
            #of the (x,y) coordinate
            
            if x < 0:
                j = x + 2
            else:
                j = x + 1
            if y > 0:
                i = -y + 2
            else:
                i = -y + 1
            return (i,j)
        
        for k in range(4):
            cipherSpots += [returnCoor(coAll[k][0],coAll[k][1])]
#        print("cipherSpots:", cipherSpots)
        return cipherSpots
    
    cipher_grille2 = [[],[],[],[]]
    cipher_grille3 = [[],[],[],[]]
    cipher_grille4 = [[],[],[],[]]
    cList = [cipher_grille, cipher_grille2, cipher_grille3, cipher_grille4]
    for i in range(4):
        for j in range(4):
            cipher_grille2[i] += ["."]
            cipher_grille3[i] += ["."]
            cipher_grille4[i] += ["."]
    #Now all of them look like this:
    #[['.', '.', '.', '.'], 
    #['.', '.', '.', '.'], 
    #['.', '.', '.', '.'], 
    #['.', '.', '.', '.']]
    
    #convert coordinates into (0,0) in the middle
    #and make the four grilles into (a+,b+), (b+,a-), (a-,b-), (b-,a+)
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == "X":
                cipherSpots = intoLoca(i,j)
                for k in range(1,4):
                    cList[k][cipherSpots[k][0]][cipherSpots[k][1]] = "X"

    #contruct returned string
    password = ""
    for grille in range(4):
        for i in range(4):
            for j in range(4):
                if cList[grille][i][j] == "X":
                    password += ciphered_password[i][j]
    return password
                
                
                
print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example')            