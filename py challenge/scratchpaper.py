# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:32:09 2017

@author: Andrew
"""

import urllib.request


req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   
print(the_page)

x = ""
x += "30982"

req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x)
with urllib.request.urlopen(req) as response:
   the_page = str(response.read())
   
print(the_page)

while True:
    for i in range(len(the_page)):
        if str(the_page[i]) in "0123456789":
            x = str(the_page[i:i+5])
            break
    req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x)
    with urllib.request.urlopen(req) as response:
        the_page = str(response.read())
   
    print(the_page)

#while the_page[:26] == "b'and the next nothing is ":
#    x = ""
#    x += the_page[26:]
#    req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x)
#    with urllib.request.urlopen(req) as response:
#        the_page = response.read()
#   
#    print(the_page)

#ANSWER: 66831