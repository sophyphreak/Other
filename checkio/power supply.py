# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 11:31:22 2017

@author: Andrew
"""
'''
Input: Two arguments. The first 
one is the network, represented 
as a list of connections. Each 
connection is a list of two nodes 
that are connected. A city or 
power plant can be a node. Each 
city or power plant is a unique 
string. The second argument is 
a dict where keys are power 
plants and values are the power 
plant's range.

Output: A set of strings. Each 
string is the name of a 
blacked out city.

Example:
power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])
'''

class Powa:
    def __init__(self, connections, power):
        self.connections = connections
        self.power = power
    
    def connected(self, a):
        '''
        input:
        string
        
        returns:
        set with all connections to string
        '''
        conReturn = []
        for entry in self.connections:
#            print('entry =',entry)
            if a in entry:
#                print('entry with a=',entry)
                for item in entry:
#                    print('item =',item)
                    if item != a:
#                        print('item not a=',item)
                        conReturn += [item]
        return conReturn
        
    def onePlantPowered(self, plant, powerNum, answer):
        '''
        input:
        string, a power plant
        int, the amount of power for that plant
        list, current partial answer
        
        output:
        partial answer string for powered cities
        '''
        while True:
            #set place for the loop to start when it goes to the first city
            index = 0 
            current = plant #current plant or city
            #loop until we run out of power
            while powerNum > 0:
                #find all connections of that power plant
                connections = self.connected(current)
                currentcon = 0 #start at index 0 of connections
                #loop until we run out of direct connections to current
                while not currentcon == len(connections):
                    #gives power to each city connected until we run out of 
                    #power and adds each powered city to answer list
                    
                    #first, opens up the connection we are working with, 
                    #sets to city variable
                    city = connections[currentcon]
                    #first, checks if city is a city
                    if city[0] == 'c':
                        #if so, then checks if it's already in answer
                        if not city in answer:
                            #if not, then adds it to answer
                            answer += [city]
                            #and subtracts one from powerNum
                            powerNum -= 1
                            #if we are out of power, return list of powered
                            #cities
                            if powerNum < 1:
                                return answer
                    currentcon += 1
                #after the loop, current changes to next city connection
                if len(answer) < index:
                    current = answer[index]
                else:
                    return answer
    
        
    def powered(self):
        '''
        input:
        nothing
        
        output:
        list of powered cities
        '''
        #create powered cities list
        answer = []
        #first, go through each power plant
        #plant is the current power plant we are working with
        #powerNum is the number of units of power that power plant has
        for plant in self.power:
#            print(answer)
            powerNum = self.power[plant]
            answer = self.onePlantPowered(plant, powerNum, answer)
#            print(answer)
        return answer

    def unpowered(self):
        '''
        input:
        nothing
        
        returns:
        set with a list inside of all unpowered cities
        '''
        answer = []
        poweredList = self.powered()
        for entry in self.connections:
            for item in entry:
                if not item in poweredList and not item[0] == 'p':
                    answer += [item]
        return answer

def power_supply(lst, dic):
    '''
    input:
    list of connected cities and power plants
    dictionary of power per power plant
    
    returns:
    set of list of unpowered cities
    '''
    stuff = Powa(lst, dic)
    answer = set(stuff.unpowered())
    return answer

print(power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}))
print(power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}))
print(power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}))

    
print(power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2']))
print(power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']))
print(power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]))
                