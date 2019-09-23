# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:38:22 2019

@author: Alok
"""

# Decision-making-statements
# while
# for

# while - is used to execute given set of instructions while condition
# is true. 
# if given condition is true it will keep on executing code, once 
# condition fail, it will stop

# syntax
# while(condition):
#   python statements
# else:
#   python statements

# else will be execute when condition os fail to satisfy. 
# else is optional

time=5
while(time<8):
    print("Good Evening")
    time+=1   # time=time+1
else:
    print("Good night")

def get_greetingmsg(time):
    while(time<8):
        print("Good Evening")
        time+=1   # time=time+1
    else:
        print("Good Night")
    return ;

get_greetingmsg(5)


# for loop - is used to execute one time for each object in given
# collection
#syntax
# for object in collection:
#   python statemets

even_no=range(2,20,2)  # range() - create series of values from given
#                                  start,stop and interval
for i in even_no:
    print(i)

mylist=[1,4,3,5,2,7]
# increment all values of mylist by 5
newlist=[]
print(newlist)
for i in mylist:
    newlist.append(i+5)

print(newlist)

# when to use for loop and when to use while loop, how we can decide
# case-1: A boy used to save 9/- per week. He want to know in a year
# how much he can accumulate.
# case -2: Same boy want 1000/-, how many days it will take to get this
# amount.

# case-1 solution
def total_amt(perweek):
    total=0
    for i in range(1,53):
        total+=perweek
    return total;

total_amt(9)
total_amt(20)

#case-2 solution
def req_days(perweek,reqamt):
    total=0; week_no=0
    while(total<=reqamt):
        total+=perweek
        week_no+=1
    return [week_no*7,total];

req_days(9,1000)

#Case-3 Ambani want to start new retail business, he need 5 lacs.
# he is able to save 15000/- per month from his current work.
# he save money in bank and bank roi=8% per annum. If interest is
# compounded monthly,then how many months he need.

def req_mont(permonth,reqamt,roi=8):
    total=0; month_no=0
    while(total<=reqamt):
        total+=permonth
        total+=total*((roi/12)/100)
        month_no+=1
        print("Month no=",month_no," Amount=",total)
    return [month_no,round(total,2)];

req_mont(15000,500000)

# loop control statements
# break      - stop loop execution
# continue   - stop current execution and continue for next
# pass       - go to next line, it has no use

for i in "PYTHON":
    print(i)
    
for i in "PYTHON":
    if(i=="T"): break
    print(i)
    
for i in "PYTHON":
    if(i=="T"): continue
    print(i)
    
for i in "PYTHON":
    if(i=="T"): pass
    print(i)
        



        










    







    

    
