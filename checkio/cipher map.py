# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 05:52:46 2017

@author: Andrew
"""
def recall_password(cipher_grille, ciphered_password):
    #input: tuples--cipher grille and ciphered password
    #returns: string, decoded password
    
    
    #construct converters
    conv1 = [(0,0), (0,3), (3,3), (3,0)]
    conv2 = [(0,1), (1,3), (3,2), (2,0)]
    conv3 = [(0,2), (2,3), (3,1), (1,0)]
    conv4 = [(1,1), (1,2), (2,2), (2,1)]
    conv = [conv1, conv2, conv3, conv4]
    #Create skeleton cipher grilles 2, 3, and 4
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
    def convSkel(i, j, conv):
        for k in range(4):
            if (i,j) == conv[k]:
                base = k
        for k in range(1, 4):
            base1 = base
            base1 += k
            if base1 > 3:
                base1 -= 4
            cList[k][conv[base1][0]][conv[base1][1]] = "X"
#        for i in range(4):
#            print(i + 1, ":")
#            for j in range(4):
#                print (cList[i][j])


    #Take the cipher grille and convert it into all requisite forms
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == "X":
                for k in conv:
                    if (i, j) in k:
                        convSkel(i, j, k)
                        
    #contruct returned string
    password = ""
    for grille in range(4):
        for i in range(4):
            for j in range(4):
                if cList[grille][i][j] == "X":
                    password += ciphered_password[i][j]
    return password
#    return ""
#recall_password(('....',
#                 '....',
#                 '....',
#                 '....'),[])
#These "asserts" using only for self-checking and not necessary for auto-testing
print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example')

print(recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example')
