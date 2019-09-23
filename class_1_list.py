# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:32:22 2019

@author: Alok
"""

# =============================================================================
# List - it is python object to store multiple values of different
# types. List is a one dimensional array.
# use [] - to create list
# =============================================================================

# ctrl+4 -  to add comment
# ctrl+5 - to remove comment

list1=[10,20,30,40,50]
print(list1)

list2=['a',10,'b',20,'c',30]
print(list2)

list3=[['a',10],['b',20],['c',30]]
print(list3)

#len(list_name) - is used to return no of values in list

print(len(list1))

print(len(list3))

len(list2)
len(list3)

# what will happen when we donot give print() function ?

# Extraction from list

print(list1[2]) # second position or index in list

# second value of list
print(list1[1])

# for more than one value, we need list slicing

# =============================================================================
# list_name[start:stop]  - all values between start and stop
#                          but exclude stop position
# list_name[start:]      - all values from given start to till end
# list_name[:stop]       - all values from 0 position till stop, but 
#                          exclude stop position
# list_name[:]           - all values of list
# 
# =============================================================================

# find 1 position to 3rd position value of list1
# find first 3 values of list1
# find last value of list1

# results
# 1. 20,30,40
# 2. 10,20,30
# 3. 50

list1[1:4]
list1[:3]
list1[-1]

# Extract value 20 from list3

list3[1][1]


# list Manipulation
# add new value to list
list1.append(60)
list1

list1.insert(2,25)
list1

# remove values
list1.remove(30)
list1

# replace value
list1[3]=15
list1

# reverse value
list1.reverse()
list1

# sort values
list1.sort()  # sorting is always in ascending order
list1

# operator Overloading
list1*3
list1+[70]




































