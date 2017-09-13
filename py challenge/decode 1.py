# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:30:29 2017

@author: Andrew
"""



class Message:
    
    def __init__(self,words):
        self.message = words
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        self.alplist = []

        for i in range(26):
            self.alplist += [self.alpha[i]]

    def shift(self,letter,num):
        if not letter in self.alplist:
            return letter
        for i in range(len(self.alplist)):
            if letter == self.alplist[i]:
                if i + num > 25:
                    return self.alplist[i+num-26]
                return self.alplist[i+num]

    def decode(self, num):
        decoded = ""
        for i in range(len(self.message)):
            decoded += self.shift(self.message[i], num)
        return decoded

                
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."                

mine = Message('pickle')
print()
print("Output:", mine.decode(2))