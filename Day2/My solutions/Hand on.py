# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:28:01 2019

@author: kk
"""

#Hands on 01
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

a = list(range(1, 20) )
for i in a: 
    print (i) 
x=a[0:20:2]    
print("odd numbers",x)  
y=a[1:20:2]    
print("even numbers",y) 
    
#Hands on 02
# Make a function to find whether a year is a leap year or no, return True or False 

year = int(input("Please Enter the Year Number: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
    
#Hands on 03
# Make a function days_in_month to return the number of days in a specific 
# month of a year

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def days_in_month(month,year):

    if month == 'September' or month == 'April' or month == 'June' or month == 'November':
        print (30)

    elif month == 'January' or month == 'March' or month == 'May' or month== 'July' or month == 'August' or month == 'October' or month== 'December':
        print (31)

    elif month == 'February':
        if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
            print (29)
        else:
            print (28)

