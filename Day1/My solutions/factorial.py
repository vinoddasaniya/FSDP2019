# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:50:11 2019

@author: kk
"""

#  Find the factorial of a number. 
factorial=1
number=int(input('enter the number'))
if number > 0:
   for i in range(1,number + 1):
       factorial = factorial*i
 
print(factorial)