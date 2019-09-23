# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:46:16 2019

@author: Alok
"""

# =============================================================================
# pandas - is a general purpose package to store multiple data of different
# types in spreadsheet style. It can perfrom various data analytics
# task such as descriptive statistics, sorting, group by, correlation etc.
# 
# =============================================================================


import numpy as np
import pandas as pd

data1=pd.Series([10,20,30,40,50])
print(data1)
print(type(data1))
print(data1.shape)

# Series is pandas package one dimensional array, to store multiple
# values of same type.

data2=pd.DataFrame({'a':[101,102,103],
                    'b':['xyz','abc','mno'],
                    'c':[100,200,300]})
print(data2)
print(type(data2))
print(data2.shape)

# DataFrame is pandas package two dimensional array, to store 
# data multiple data of different types.
# Each key of dataframe must have same number of values

# Broadcasting
data3=pd.DataFrame({'x':data1,
                    'y':100,
                    'z':200})
print(data3)

#Note - You can create a data frame with different number of 
# values under each column, but this is allowed for single value
# only.

employee=pd.DataFrame({
        'Id':range(101,106),
        'Name':['Ravi','Mona','Rabina','Mohan','Ganesh'],
        'Sex':['M','F','F','M','M'],
        'Age':[20,22,24,26,28],
        'Salary':[20000,22000,24000,26000,28000]})

print(employee)
print(employee.shape)   # return dimension of dataframe
print(employee.columns) # return column names of dataframe
print(employee.head(3)) # return top 3 rows(observation), 
                        # default is 5
print(employee.tail(3)) # return botton 3 row, default is 5
print(employee.describe()) # return descriptive statistics for
                            # for all numeric variables

# Extraction
employee['Name']                            
employee.Name

employee[['Name','Age']] # column values

employee[0:3] # rows values or index values

# first three names
employee['Name'][0:3]
employee.iloc[0:3,1]
# iloc = index location

# class assignment
# find salary of Mona
# find salary of Mona and Ganesh
# find name of employee whose salary is highest

employee[employee['Name']=='Mona']['Salary']

employee[employee['Name'].isin(['Mona','Ganesh'])][['Name','Salary']]

np.max(employee['Salary'])

#Manipulation
# adding new column
employee['bonus']=employee['Salary']*(30/100)
print(employee)

# Dropping column
employee2=employee.drop(['Age'],axis=1)
print(employee2)

# transposing data frame
employee.transpose()

# sorting dataframe
employee.sort_values(by='Salary',ascending=False)
# sorting data frame in descending order

# group by calculation
employee.groupby(by='Sex').mean()
# find mean for all numeric variable for each group of 
# Sex

employee.groupby(by='Sex')['Salary'].mean()
# find mean salary for each group of Sex

# updating column values
new_salary=employee['Salary']*1.05

#employee['Salary']=employee['Salary']*1.05

# class assignment
# how many employees have salary above 25k
# average salary for employee whose salary is above 25k
# average salary for female employee only
# drop observation or row for Mona
# add new observation, take values of your choice

#ans-1
(employee['Salary']>25000).sum()
#ans-2
above_25k=(employee['Salary']>25000)
employee[above_25k]['Salary'].mean()

#ans-3
employee[employee.Sex=="F"]['Salary'].mean()

#ans-4
employee3=employee[employee['Name']!='Mona']
employee3

#ans-5
print(employee)
newrow=pd.DataFrame({'Id':[105],
                    'Name':['Ganesh'],
                    'Sex':['M'],
                    'Age':[28],
                    'Salary':[28000],
                    'bonus':[8400.0]})

pd.concat([employee,newrow],axis=0)

# Python test is scheduled on 14th Aug 2019 at 4:30 PM
# tomorrow we have doubts session.









































