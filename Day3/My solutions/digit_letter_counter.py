# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:11:31 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate
    the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

string = input('Enter a string')
d=l=0
for i in string:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("Digits", d)
print("Letters", l)    