# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 09:22:30 2017

@author: Andrew
"""

class Friends:
    def __init__(self, connections):
        '''
        input:
        a tuple of sets with two items in each set
        
        returns:
        nothing
        '''
        self.connections = connections
        
    def getConnections(self):
        '''
        input:
        nothing
        
        returns:
        tuple of sets
        '''
        return self.connections
        
    def add(self, connection):
        '''
        input:
        set of two strings
        
        returns:
        boolean True if this set already exists in object, False otherwise
        '''
        if connection in self.connections:
            return False
        else:
            self.connections += (connection,)
            return True
    
    def __repr__(self):
        answer = str(self.connections)
        return answer
            
    def remove(self, connection):
        '''
        input:
        set of two strings
        
        returns:
        boolean True if this connection exists, False otherwise
        '''
        if connection in self.connections:
            temp = self.connections[:]
            self.connections = ()
            for i in temp:
                if not connection == i:
                    self.connections += (i,)
            return True
        else:
            return False
    
    def names(self):
        '''
        input:
        nothing
        
        returns:
        set of names
        '''
        answer = set()
        for entry in self.connections:
            if len(entry) == 2:
                for item in entry:
                    if not item in answer:
                        answer.add(item)
        return answer
        
    def connected(self, a):
        '''
        input:
        string
        
        returns:
        set with all connections to input
        '''
        answer = set()
        for entry in self.connections:
            if a in entry:
                for item in entry:
                    if item != a:
                        answer.add(item)
        return answer