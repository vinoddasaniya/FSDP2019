# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:57:19 2019

@author: kk
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re
while True:
    input_numbers = input("Enter the numbers")
    
    if not  input_numbers:
        break
    if re.match(r'^[+-]?[0-9]+\.[0-9]+' ,input_numbers):
        print('True')
    else:
        print('False')
        
    
    