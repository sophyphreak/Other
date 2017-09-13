# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:36:04 2017

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

    monthLengths = []
    monthLengthsLeap = []
    for i in months:
        monthLengths += [len(i)]
    for i in monthsLeap:
        monthLengthsLeap += [len(i)]
                      
    date1 = list(date1)
    date2 = list(date2)
    
    if date1[0] % 4 == 0:
        m = monthLengthsLeap
    else:
        m = monthLengths
    
    if (date1[0] % 400 != 0 and date1[0] % 100 == 0):
        m = monthLengths
        
    nthDay1 = 0    
    
    for i in range(date1[1]-1):
        nthDay1 += m[i]
    nthDay1 += date1[2]




    if date2[0] % 4 == 0:
        m = monthLengthsLeap
    else:
        m = monthLengths

    if (date2[0] % 400 != 0 and date2[0] % 100 == 0):
        m = monthLengths
            
    nthDay2 = 0    
    
    for i in range(date2[1]-1):
        nthDay2 += m[i]
    nthDay2 += date2[2]
  
    if date1[0] == date2[0]:
        daysDiff = nthDay2 - nthDay1
        return daysDiff
    else:
        daysDiff = nthDay2 - nthDay1
        for i in range(date1[0], date2[0]):
            if i % 4 == 0 and not (i % 400 != 0 and i % 100 == 0):
                daysDiff += 366
            else:
                daysDiff += 365

    return daysDiff

print(days_diff((1,1,1), (9999,12,31)))