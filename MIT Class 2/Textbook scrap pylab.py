# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:56:05 2017

@author: Andrew
"""
import pylab

##set line width
#pylab.rcParams['lines.linewidth'] = 4
##set font size for titles
#pylab.rcParams['axes.titlesize'] = 20
##set font size for labels on axes
#pylab.rcParams['axes.labelsize'] = 20
##set size of numbers of x-axis
#pylab.rcParams['xtick.labelsize'] = 16
##set size of numbers on y-axis
#pylab.rcParams['ytick.labelsize'] = 16
##set size of ticks on x-axis
#pylab.rcParams['xtick.major.size'] = 7
##set size of ticks on y-axis
#pylab.rcParams['ytick.major.size'] = 7
##set size of markets, e.g., circles representing points
#pylab.rcParams['lines.markersize'] = 10
##set number of times market is shown when displaying legend
#pylab.rcParams['legend.numpoints'] = 1

#pylab.figure(1)         
#pylab.plot([1,2,3,4], [1,2,3,4])
#pylab.figure(2)
#pylab.plot([1,4,2,3],[5,6,7,8])
#pylab.savefig('Figure-Addie')
#pylab.figure(1)
#pylab.plot([5,6,10,3])
#pylab.savefig('Figure-Jane')

#principle = 10000 #initial investment
#interestRate = .05
#years = 20
#values = []
#for i in range(years + 1):
#    values.append(principle)
#    principle += principle*interestRate
#pylab.plot(values, 'ko')
#pylab.title('5% Growth, Compounded Annually')
#pylab.xlabel('Years of Compounding')
#pylab.ylabel('Value of Principal($)')

#principal = 10000 #initial investment
#interestRate = 0.05
#years = 20
#values = []
#
#for i in range(years + 1):
#    values.append(principal)
#    principal += principal*interestRate
#pylab.plot(values)
#pylab.title('5% Growth, Compounded Annually', fontsize = 'xx-large')

def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
        
    def getTotalPaid(self):
        return sum(self.paid)
    def __str__(self):
        return self.legend
    
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
                   
    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)
        
    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            pylab.plot(totPd, style, label = self.legend)
                       
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * \
                                     len(self.outstanding))
        equityAcquired = equityAcquired - \
                         pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)