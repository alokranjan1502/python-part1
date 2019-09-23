# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:08:24 2019

@author: Alok
"""

# =============================================================================
# Function - is used to perfrom specific calculation and return value.
# Like variable and objects, function is also temporary. this means you
# can use your defined function for only one session.
# Syntax
# def function_name(args):
#     python statements
#     return var;
# 
# In order to use function, you have to call it
# 
# function_name(values)
# 
# =============================================================================

def add2no(x,y):
    total=x+y
    return total;


add2no(10,20)
print(add2no(20,30))
add_result=add2no(30,40)
print(add_result)

# Write a function to find total amount to be paid by customer after
#10% discount. 

# Hey what we have to do ? 
# you do first, i will copy. or i will wait for sir to write code.

def final_amount(amount):
    discount=amount*(10/100)
    finalamt=amount-discount
    return finalamt;

final_amount(100)


def get_finalamt(amount,discount=10):
    discount=amount*(discount/100)
    finalamt=amount-discount
    print(discount)
    return finalamt;

get_finalamt(100)
get_finalamt(100,20)
get_finalamt(100,30)

# local and global variable
# local variable - a variable created within function, these variable
# cannot accessiable outside function
# global variable - a variable created outside function, and these
# variables can be used any where.

# Can we use global variable within function ? Yes
# can we use local variable outside function ? No

print(discount)

x = 200
def increment(amt):
    newamt=amt+x
    return newamt;


increment(100)

# Write a python function to convert first N character of given name 
# into upper case and rest should be in lower case, if N is not given
# then take n=1

# alok - Alok or abhishek  - Abhishek

# can we apply function on list ? yes, then create some exaple for it
# no - no need for any example - we discuss this later


def first_upper(name,n=1):
    f1=name[0:n].upper()
    f2=name[n:].lower()
    newname=f1+f2
    return newname;

first_upper("ALOK",4)
first_upper("Philip")

# Decision Making statements
# if
# where
# for

# if statement - is used to perfrom calculation when given condition
# is true
#type-1  if (condition): action1
#type-2  if (condition):
#           action1
#           action2
#type-3 if (condition1):
#           action1
#       elif (condition2):
#           action2
#       else:
#           action3

# write python code to display result as PASS if marks is above 50,
# otherwise FAIL

marks=5; result="FAIL"
if (marks>50): result="PASS"
print(result)

# you can take input from user as well

name=input("Please enter your name")
marks=int(input("Please enter your marks"))
#print(name,marks)
result="FAIL"
if (marks>50): result="PASS"
print(name,", your result is ", result)

# class assignment
# write python code to find square and square root of user given x,
# if x is more than 5 and less than 10.
import math
x = int(input("Enter positive numeric value" ))
sq=0
sr=0.0
if ((x>5) & (x<10)):
    sq=x*x
    sr=math.sqrt(x)
print("Result is ")
print(sq,round(sr,2))

# Write python code to find square of x if x is less than 10, and 
# find square root of x if x is between 10 and 20, Display X as it is
# if it is more than 20.

def get_req_value(x):
    if (x<10):
        result=x*x
    elif (x<20):
        result=round(math.sqrt(x),2)
    else:
        result=x
    return result;

get_req_value(2)
get_req_value(12)
get_req_value(22)
