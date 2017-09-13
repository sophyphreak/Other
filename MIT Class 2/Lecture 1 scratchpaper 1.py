# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 01:31:21 2017

@author: Andrew
"""

class item(object):
    def __init__(self, name, value, weight):
        #create an item with a name, value, and weight
        self.name = name
        self.value = value
        self.weight = weight
    def getName(self):
        #returns name of item
        return self.name
    def getValue(self):
        #returns value of item
        return self.value
    def getWeight(self):
        #returns weight of item
        return self.weight
    def getRatio(self):
        #returns ratio of value to weight
        return self.value/self.weight
    def __repr__(self):
        return self.name
        
class knapsack(object):
    def __init__(self, name, maxWeight):
        #creates a knapsack with a name and a max weight
        self.name = name
        self.maxWeight = maxWeight
        self.weight = 0
        self.value = 0
        self.itemsInside = []
    def getName(self):
        #returns name of knapsack
        return self.name
    def getMaxWeight(self):
        #returns max weight of knapsack
        return self.maxWeight
    def getWeight(self):
        #returns current weight of items in knapsack
        return self.weight
    def getValue(self):
        #returns current value of items within knapsack
        return self.value
    def printItemsInside(self):
        #prints list of names of items inside knapsack
        print("Items:")
        for i in self.itemsInside:
            print(self.getName())
    def getItemsInside(self):
        #returns list of items inside
        return self.itemsInside
    def getRatio(self):
        #returns ratio of value/weight
        return self.value/self.weight
    def addItem(self, item):
        #adds an item to the knapsack
        if self.getWeight() + item.getWeight() <= self.getMaxWeight():
            self.itemsInside += [item]
            self.weight += item.getWeight()
            self.value += item.getValue()
    def removeItem(self, item):
        #removes an item from the knapsack
        tempStr = []
        for i in self.getItemsInside():
            tempStr += [i]
        if item in tempStr:
            tempStr.remove(item)
        self.itemsInside = tempStr
    def checkCanFit(self, item):
        if self.getWeight() + item.getWeight() > self.getMaxWeight():
            return False
        else:
            return True

def optimize(itemList, knapsack):
    itemList1 = []
    for i in itemList:
        itemList1 += [i]
    ratioList = []
    for item in itemList1:
        ratioList += [item.getRatio()]
    while len(itemList1) > 0:
        maxRatioSpot = 0
        maxRatio = 0
        for i in range(len(ratioList)):
            if ratioList[i] > maxRatio:
                maxRatio = ratioList[i]
                maxRatioSpot = i
#        print("itemList1:", itemList1)
#        print("maxRatioSpot:", maxRatioSpot, "of", len(itemList1))
#        print("ratioList:", ratioList)
#        print("item:", itemList1[maxRatioSpot])
#        print()
        if knapsack.checkCanFit(itemList1[maxRatioSpot]) and \
                                itemList1[maxRatioSpot].getValue() > 0:
            knapsack.addItem(itemList1[maxRatioSpot])
        ratioList.remove(maxRatio)
        itemList1.remove(itemList1[maxRatioSpot])
        
    


clock = item("clock", 175, 10)
picture = item("picture", 90, 9)
radio = item("radio", 20, 4)
vase = item("vase", 50, 2)
book = item("book", 10, 1)
computer = item("computer", 200, 20)

itemList = [clock, picture, radio, vase, book, computer]

ratioList = []
for item in itemList:
    ratioList += [item.getRatio()]

bag = knapsack("bag", 20)

optimize(itemList, bag)