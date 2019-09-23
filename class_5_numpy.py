# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:04:30 2019

@author: Alok
"""

# i have a question for you.
# write python code to find 10 even number starting from user 
# given value
# store all even values into a list. 

def get_even_values(x):
    if (x % 2!=0): x+=1
    newlist=[]
    for i in range(1,11):
        newlist.append(x)
        x+=2
    return newlist;

get_even_values(3)        


# Package - is a compress file which include multiple function.
# In order to use function of a package we need to install it
# first and then import in current program.
# How to install package ? 1. GUI, 2. command prompt

import package_name as alias # this import all function of given
# package.(module)

from package_name import function_name # this will import 
# only one function of given package

# How to use import functions
 # alias.function_name()  # when you import complete package
 # function_name()        # when you import one function
 
 # all import of functions will be available for only one 
 # session
 
 import numpy as np
# =============================================================================
# numpy - numpy is python package to perfrom all sort of 
# numeric calculation.
# It works with only numeric values and store values of 
# same type in an object
# 
# numpy store data in the form of array and it is called
# ndarray. ndarray - n dimensional array
# 
# =============================================================================

data1=np.array([10,20,30,40,50])
print(type(data1))
print(data1)

# extraction of data from np.array() is same as list extraction
data1[0]   # extract first value
data1[-1]  # extract last value
data1[2:4] # extract 2 and 3rd value
# class assignment
# extract all values excluding first and last value
data1[1:-1]

# 2-dimensional array
data2=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(data2)
print(data2.shape)
print(data2[2,2])

# Rows    - index   - observations - axis=0
# Columns - columns - variables    - axis=1

#class assignment
# create two dimensional array of shape (5,2) with below given data
# 20,22,24,26,28,30,32,34,36,38

# create two dimensional array of shape (3,4) with 
# first 12 even values.

data3=np.array([20,22,24,26,28,30,32,34,36,38])
data3.shape
data3A=data3.reshape(5,2)
print(data3A)
data3A.shape

data4=np.array(range(2,26,2))
data4.shape
data4A=data4.reshape(3,4)
data4A.shape
print(data4A)

#Array Manipulation
#1. find total
np.sum(data4A)
np.sum(data4A,axis=0)  # axis=0  means row/index values
np.sum(data4A,axis=1)  # axis=1  means columns values

np.add(data4A,10)      # add 10 to each value of array

np.mean(data4A,axis=1)  # axis=1 means column/variable values

#2. transpose
np.transpose(data4A)

#3. sorting data
data5=np.array([100,75,30,120,130,90])
np.sort(data5)

#class challenge question
# how to get descending order sorting ?
-np.sort(-data5)

#4. how to add new value
# add new value 110 to data5
np.append(data5,110)

#5. how to remove value from array
# remove 30 from data5
np.remove(data5[2])  # syntax error, reason remove is part
# of list function, not array function
np.delete(data5,[2])

#6. replace value inside array
# replace 75 to 80
data5[1]=80

print(data5)
# =============================================================================
# Test date - 14th Aug 2019
# topics - till 12th Aug 2019 topics
# 13th Aug 2019 - practice and doubt session
# =============================================================================






























