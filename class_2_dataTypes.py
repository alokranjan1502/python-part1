# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:38:18 2019

@author: Alok
"""

# Data Types - different types of values python can store
# there are 5 different types of values
# 1. integer or int - a numeric value without decimal
# 2. float - a numeric value with decimal
# 3. string - any value with quotation 
# 4. boolean - True or False
# 5. complex - a+bj - a=real value and b=imaginary value
# j^2 = -1

# to store multiple values, there are three different
# types of objects
# 1. list     - mutable - []
# 2. tuple    - immutable - ()
# 3. dictionary - store value in key:value pair - {}

i1=10
f1=10.5
# type() - return data type of given variables
type(i1)
type(f1)

total = i1 + f1
total
# you can use arethmetic operator on integer and float
# values.

#int() and float() - are conversion function, to get
#values of its own type
int(f1)
float(i1)

s1="python"
s2="LEARN"

# strings are stored as string list.
print(s1,s2)
# function used on string values
# str.lower() - return lower case value
# str.upper() - return upper case value
s1.upper()
s1+s2
s1+" "+s2
# Using s1 and s2, create value "Learn Python"
s2[0].upper()+s2[1:].lower()+" "+s1[0].upper()+s1[1:].lower()

s2.capitalize()+ " " + s1.capitalize()

# boolean value - is created when you use condition
# or directly store values
b1=True
b2=10==12

type(b1)
type(b2)

# and
b1 & b2

# or 
b1 | b2

#not equal to
b1 != True

complex1=1+2j
complex2=2+3j

complex1+complex2 # 3+5j

complex1*complex2 # -4+7j
# 2*1+2*2j+3j*1+3j*2j = 2+4j+3j-6=-4+7j

mylist=[10,20,30]
mytuple=(10,20,30)
mydict={'a':10,'b':20,'c':30}

print(mylist,mytuple,mydict)

# replace 20 to 25 in all three object
mylist[1]=25
mydict['b']=25
mytuple[1]=25  # syntax error
# in order to change value, we need to create tuple
# again
mytuple=(10,25,30)

print(mylist,mytuple,mydict)

# tuple is used to store constant values, whose values
# does not change frequently.

# working with dictionary
# to know all keys
mydict.keys()  # keys should be unique in dictionary
# and it can be numeric or character

#to know all values
mydict.values()

# to add new values to dictionary
mydict['d']=40
print(mydict)

# to remove values in dictionary
mydict['b']=[]
print(mydict)

# to delete key:value pair in dictionary
del mydict['b']
print(mydict)

# can be store more than one value to key of dictionary
# yes you can store more than one value to each keys()

# can we store unequal values in each keys ?
# yes you can store different number of values
mydict2={'a':[1,2,3],'b':[4,5]}
mydict2

mydict3={'1':['a','b'],'2':[1,2,3]}
mydict3





