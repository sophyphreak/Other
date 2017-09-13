# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 04:43:48 2017

@author: Andrew
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 03:31:42 2017

@author: Andrew
"""
# round(number[, ndigits])

# (3329, 310)
# (4773, 440)
# (3926, 360)

balance = 4773
annualInterestRate = .2


monthlyInterestRate = annualInterestRate / 12
monthlyUnpaidBalance = balance
updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate 
                                                  * monthlyUnpaidBalance)

time = 12 #months


def creditCard(balance, monthlyInterestRate, monthlyUnpaidBalance, payment, time):
    if (time == 0):
        return balance
    else:
#        print("original balance: " + str(balance))
        
        monthlyUnpaidBalance = balance - (payment)
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        time -= 1
        
#        print("payment: " + str(payment))
#        print("monthlyUnpaidBalance: " + str(monthlyUnpaidBalance))
#        print("monthlyInterestRate: " + str(monthlyInterestRate))
#        print("time: " + str(time))
#        print("new balance: " + str(balance))
#        print("")
#        print ("Month " + str(abs(12-time)) + "  Remaining balance: " + str(round(balance, 2)))
        return creditCard(balance, monthlyInterestRate, monthlyUnpaidBalance, payment, time)

#balance = creditCard(balance, annualInterestRate, monthlyUnpaidBalance, payment, 12)

#print(balance)
        
low = balance / 12
high = (balance * (1 + monthlyInterestRate)**12) / 12
payment = (low + high) / 2
        
def paymentCalc(balance, monthlyInterestRate, low, high, payment):
    if abs(creditCard(balance, monthlyInterestRate, monthlyUnpaidBalance, payment, 12)) < .0001:
        return round (payment, 2)
    else:
#        print ("year-end balance: " + str(creditCard(balance, monthlyInterestRate, payment, 12)))
        if creditCard(balance, monthlyInterestRate, monthlyUnpaidBalance, payment, 12) > 0:
            low = payment
            payment = (low + high) / 2
        else:
            high = payment
            payment = (low + high) / 2
#        print("payment guess = " + str(payment))
        return paymentCalc(balance, monthlyInterestRate, low, high, payment)

payment = paymentCalc(balance, monthlyInterestRate, low, high, payment)
        
print("Lowest Payment: " + str(payment))