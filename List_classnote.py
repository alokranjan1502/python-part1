# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:31:38 2019

@author: Alok Ranjan
Topics: List
"""

# =============================================================================
# Create a list call it Pricelist with below given values
# 100,110,120,128,140,150
# 
# 1. Find 3rd value of pricelist
# 2. find first three values
# 3. find last three values
# 
# =============================================================================

pricelist=[100,110,120,128,140,150]
print(pricelist)

print(pricelist[2])
print(pricelist[:3])
print(pricelist[-3:])

# List Manipulation
#1. Adding new value to list

pricelist.append(160)
print(pricelist)

#2. remove value from list
pricelist.remove(120)
print(pricelist)

#3. find position of given value
pricelist.index(128)

#4. insert new value to specific position
pricelist.insert(2,125)
print(pricelist)

#5. reverse values of list
pricelist.reverse()
print(pricelist)

#6. sort values of list
pricelist.sort()  # default sorting order is ascending order
print(pricelist)

# Class Assignment
# create a list with even number between 20 to 30.
# find 2nd to 4th value of list
# replace 2nd value with 23
# add new value 32 in the last
# sort data in descending order


evenno=list(range(20,31,2))  
#range() - return set of values from given start, stop and interval
print(evenno)
#1
print(evenno[1:4])
#2
evenno[1]=23
print(evenno)
#3
evenno.append(32)
print(evenno)
#4
evenno.reverse()
print(evenno)

#Nested list
Weekly_pricelist=[['mon',100],['tue',110],['wed',120],
                  ['thu',128],['fri',140]]
print(Weekly_pricelist)

# find 2nd value of given list
# find 2nd sub value of 2nd elemnet
# replace 128 by 130
# add new value to list ['sat',150]
# delete ['tue',110]

print(len(Weekly_pricelist))
#1
print(Weekly_pricelist[1])
#2
print(Weekly_pricelist[1][1])
#3
Weekly_pricelist[3][1]=130
print(Weekly_pricelist)
#4
Weekly_pricelist.append(['sat',150])
print(Weekly_pricelist)
#5
Weekly_pricelist.remove(['tue',110])
print(Weekly_pricelist)

Weekly_pricelist[3].index(140)

myname="iamalok"
len(myname)
myname[-1]










































