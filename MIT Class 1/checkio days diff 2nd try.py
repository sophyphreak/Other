# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:19:21 2017

@author: Andrew
"""

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
    
    list1 = list(date1)
    list2 = list(date2)
    
    count = ()
    
        
    return daysDiff
    
print(days_diff((2014, 1, 1), (2014, 8, 27)))
