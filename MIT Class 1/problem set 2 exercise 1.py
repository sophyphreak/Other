# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 02:45:14 2017

@author: Andrew
"""
# round(number[, ndigits])

balance = 484
annualInterestRate = .2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
monthlyUnpaidBalance = balance
updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate 
                                                  * monthlyUnpaidBalance)

time = 12 #months

def creditCard(balance, monthlyInterestRate, monthlyPaymentRate, time):
    if (time == 0):
        return round(balance, 2)
    else:
        monthlyUnpaidBalance = balance - (balance * monthlyPaymentRate)
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        time -= 1
#        print ("Month " + str(abs(12-time)) + "  Remaining balance: " + str(round(balance, 2)))
        return creditCard(balance, monthlyInterestRate, monthlyPaymentRate, time)

balance = creditCard(balance, monthlyInterestRate, monthlyPaymentRate, time)
        
print("Remaining balance: " + str(balance))