###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    answer = []
    shipCows = {}
    homeCows = {}
    currentCows = {}
    for i in cows:
        homeCows[i] = cows[i]
        currentCows[i] = cows[i]
    
    def checkFit(cowValue, space):
        '''
        input:
        int-the weight of the cow you want to check if it fits
        int-the remaining space on ship
        
        returns:
        boolean-True if it can fit, False if it can't
        '''
        if cowValue > space:
            return False
        else:
            return True
    
    def nextCow(currentCows, space):
        '''
        input:
        dictionary with all the cows that are left
        amount of space left on ship
        
        function deletes cow from currentCows
            
        returns:
        list containing (1)dictionary of next cow if another cow fits
                        (2)new currentCows dictionary
        int 0 if no more cows fit
        '''
        while len(currentCows) > 0:
            maxCowKey = ""
            maxCowValue = 0
            for j in currentCows:
                if currentCows[j] > maxCowValue:
                    maxCowValue = currentCows[j]
                    maxCowKey = j
            if checkFit(maxCowValue, space):
                del(currentCows[maxCowKey])
                return [{maxCowKey:maxCowValue}, currentCows]
            else:
                del(currentCows[maxCowKey])
        return 0
    
    def addShipCow(cow, shipCows):
        '''
        input:
        dictionary with length of 1 containing cow and cow weight
        list with current cows in ship
        
        returns:
        new shipCows dictionary
        '''
        for i in cow:
            shipCows += [i]
        return shipCows
    
    while len(homeCows) > 0:
        shipCows = [] #new ship
        space = limit
        currentCows = {}
        for i in homeCows:
            currentCows[i] = homeCows[i] #reset currentCows
        tempCow = ""
        while tempCow != 0: #while there are still eligible cows
            tempCow = nextCow(currentCows, space)
            if tempCow == 0:
                break
            currentCows = {}
            currentCows = tempCow[1]
            tempCow = tempCow[0]
            shipCows = addShipCow(tempCow, shipCows)            
            for i in tempCow:
                space -= tempCow[i]
        #send off ship by adding shipCows list to answer list of lists
        #and deleting shipping cows from homeCows
        for i in shipCows:
            del(homeCows[i])
        answer += [shipCows]
    
    #everything is done. Return answer list of lists
    return answer

    
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowList = []
    for i in cows:
        cowList += [i]
    part = get_partitions(cowList)
    possibles = []
    
    def testPart(cows, limit, tempAnswer):
        '''
        input:
        dictionary cows
        int limit
        list answer
        
        returns:
        boolean. True if the partition is possible, False if it is not possible
        '''
        for i in range(len(tempAnswer)):
            mass = 0
            for j in tempAnswer[i]:
                mass += cows[j]
            if mass > limit:
                return False
        return True    
        
    tempAnswer = []
    while len(tempAnswer) < len(cowList):
        tempAnswer = next(part)
        if testPart(cows, limit, tempAnswer):
            possibles += [(tempAnswer,len(tempAnswer))]
    minLen = 1000
    answer = []
    for i in possibles:
        if i[1] < minLen:
            minLen = i[1]
            answer = i[0]
    return answer
            
        
#        
#test = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
#limit = 10
#print(brute_force_cow_transport(test, limit))
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    
    start = time.time()
    greedy = len(greedy_cow_transport(cows, limit))
    end = time.time()
    print('Greedy')
    print('Number of trips:', greedy, '  How long:', end-start, 'seconds')
    
    start = time.time()
    brute = len(brute_force_cow_transport(cows, limit))
    end = time.time()
    print('Brute')
    print('Number of trips:', brute, '  How long:', end-start, 'seconds')
    
compare_cow_transport_algorithms()

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print(cows)
#print()

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
#print(brute_force_cow_transport({'Miss Bella': 25, 'Horns': 25, 'Boo': 20, 'Lotus': 40, 'Milkshake': 40, 'MooMoo': 50}, 100))

