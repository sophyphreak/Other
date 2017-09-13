# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:09:53 2017

@author: Andrew
"""

# Using the matrix from open labrynth problem, find the DFS shortest path 
# solution

class Node(object):
    def __init__(self, name, x, y):
        """Assumes name is a string"""
        self.name = name
        self.loc = (x, y)
    def getName(self):
        return self.name
    def getLoc(self):
        return self.loc
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
    
class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def getNodes(self):
        return self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:1] #omit final newline
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
#----------------------------------------

#Shortest Path: Depth-First Search and Breath-First Search

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shorest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(path))
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)

#-----------

def testSP(matrix):
    nodes = []
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            if matrix[row][item] == 0:
                nodes.append(Node(str((row, item)), row, item))
    g = Graph()
    for n in nodes:
        g.addNode(n)
    nodes = g.getNodes()
    for item in nodes:
        if item.getLoc() == (1, 1):
            start = item
        if item.getLoc() == (10, 10):
            end = item
    for src in nodes:
        for dest in nodes:
            srcLoc = src.getLoc()
            destLoc = dest.getLoc()
            if (destLoc[0] == srcLoc[0] + 1 and destLoc[1] == srcLoc[1]) or\
               (destLoc[0] == srcLoc[0] - 1 and destLoc[1] == srcLoc[1]) or\
               (destLoc[0] == srcLoc[0] and destLoc[1] == srcLoc[1] + 1) or\
               (destLoc[0] == srcLoc[0] and destLoc[1] == srcLoc[1] - 1):
                   g.addEdge(Edge(src, dest))
#    sp = shortestPath(g, start, end, toPrint = True)
#    print('Shortest path is', printPath(sp))
    sp = BFS(g, start, end)
    print('Shortest path found by BFS:', printPath(sp))


matrix = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 2, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

testSP(matrix)
             
def checkio(maze_map):
    testSP(maze_map)
    
checkio(matrix)
                
    
    
    
    
    
    
    
    
    