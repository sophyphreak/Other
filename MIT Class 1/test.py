# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:31:14 2017

@author: Andrew
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
#plt.figure('cub')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
plt.ylabel('quadratic function')