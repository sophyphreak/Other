# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:45:03 2017

@author: Andrew
"""

from tkinter import *

top = Tk()
L1 = Label(top, text = "Tax Calculator")
L1.pack(side = TOP)
L2 = Label(top, text = "Tax rate:")
L2.pack(side = LEFT)
E1 = Entry(top, bd = 4)
E1.pack(side = RIGHT)
L4 = Label(top, text = "")
L4.pack(side = TOP)
L3 = Label(top, text = "Total price:")
L3.pack(side = LEFT)


top.mainloop()