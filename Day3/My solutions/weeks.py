# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:34:45 2019

@author: kk
"""
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


list1 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#input1 = input('input_Days_Name')
list2 =['Mon', 'Tue', 'Wed'] #input1.split()
for i in list1:
    if i not in list2:
        list2.append(i)
        print(list2)





