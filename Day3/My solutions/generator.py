# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:14:09 2019

@author: kk
"""
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""


input1 = input('Enter Values')
list1 = input1.split(",")
tuple1 = tuple(list1)
print('List1',list1)
print('Tuple1',tuple1)