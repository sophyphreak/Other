# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:36:54 2017

@author: Andrew
"""

import pickle

a = ['test value','test value 2','test value 3']
a
['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)   

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'r')  
# load the object from the file into var b
b = pickle.load(fileObject)  
b
['test value','test value 2','test value 3']
a==b
True