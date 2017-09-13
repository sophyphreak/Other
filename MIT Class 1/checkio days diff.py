# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:10:28 2017

@author: Andrew
"""

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    daysDiff = 0
    daysTup = ()
    jan = ()
    feb = ()
    feb2 = ()
    mar = ()
    apr = ()
    may = ()
    jun = ()
    jul = ()
    aug = ()
    sep = ()
    octo = ()
    nov = ()
    dec = ()
    year = []
    
    for i in range(1, 32):
        jan += (i,)
        mar += (i,)
        may += (i,)
        jul += (i,)
        aug += (i,)
        octo += (i,)
        dec += (i,)
    
    for i in range(1, 31):
        apr += (i,)
        jun += (i,)
        sep += (i,)
        nov += (i,)
        
    for i in range(1, 29):
        feb += (i,)
        
    for i in range(1, 30):
        feb2 += (i,)

        
    if date1[0] > date2[0]:
        temp = date1
        date1 = date2
        date2 = temp
    if date1[0] == date2[0]:
        if date1[1] > date2[1]:
            temp = date1
            date1 = date2
            date2 = temp
        if date1[1] == date2[1]:
            if date1[2] > date2[2]:
                temp = date1
                date1 = date2
                date2 = temp
            if date1[2] == date2[2]:
                return 0
         
    months = (jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
    monthsLeap = (jan, feb2, mar, apr, may, jun, 
                   jul, aug, sep, octo, nov, dec)
        
#    for i in range(0, 3000):
#        if i % 4 == 0:
#            year += ((monthsLeap))
#        if i % 4 != 0:
#            year += ((months))
     
#    def leftDays(date1, endpoint):
#        
#        daysTup = ()
#        
#        if date1[0] % 4 == 0:
#            m = monthsLeap
#        else:
#            m = months
#        
#        daysTup = m[date1[1]][date1[2]:len(m[date1[1]])] 
#        
#        for i in range(date1[1], endpoint)
#            
#        
#        return daysTup
#    
#    if date1[0] < date2 [0]:
#        endpoint = 12
#    else:
#        endpoint = 
#        
#    daysTup += leftDays(date1, endpoint)
    
            
            
            
            
            
            
            
            
    if date2[0] > date1[0]:
        for i in range(date1[1]-1, 12):
            for j in range(year[date1[0]][date1[1]][date1[2]], 
                           len(year[date1[0]][date1[1]])):
                daysDiff += 1
                
        tempYear = date1[0] + 1
    else:
        tempYear = date2[0]
                
    while tempYear < date2[0]:
        for i in range(len(year[tempYear])):
            for j in range(len(year[tempYear][i])):
                daysDiff += 1
        tempYear += 1
        # in the following instance, I want to count the days from date2's
        # Jan 1st to date2. I'm doing this by iterating through all the months
        # of the year with i and iterating all the days in each of those months
        # with j. For each of those, I add 1 to daysDiff. 
        
        # After this, I will count the number of days remaining in the month of 
        # date2, but not yet.
    for i in range(date2[1]):
        for j in range(len(year[date2[0]][i])):
            daysDiff += 1
    
    daysDiff += date2[2]
    
    
    return daysDiff
    
print(days_diff((2014, 1, 1), (2014, 8, 27)))
