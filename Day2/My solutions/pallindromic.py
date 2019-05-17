# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:33:46 2019

@author: kk
"""
# You are given a space separated list of integers. 
# If all the integers are positive and if any integer is a palindromic integer, 
# then you need to print True else print False.
# (Take Input from User)


my_string=input("Enter string:")

if(my_string==my_string[::-1]):
    
   print("True (The string is a palindrome)")
   
else:
    
   print("False (The string is not a palindrome)")
   