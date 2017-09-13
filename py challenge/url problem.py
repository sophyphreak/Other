# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:15:43 2017

@author: Andrew
"""

import urllib.request

html = 'and the next nothing is 44827'

print(html[24:])

#while html[:24] == 'and the next nothing is ':
if True:
    x = html[24:]
    response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ \
                                      linkedlist.php?nothing=12345')
    html = response.read()
    print(html)
print("end", html)