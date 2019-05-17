# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:16:05 2019

@author: kk
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of 
    characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

string1 = input('Enter The String')
freq = {} 
  
for i in string1: 
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1