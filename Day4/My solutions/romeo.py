# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:57:53 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

list1=[]
dic1={}
with open("romeo.txt", "rt") as f:
    for i in f:
        words = i.split()
        list1.append(i)
        for a in words:
            if a not in dic1:
                dic1[a]=1
            else:
                dic1[a]=dic1[a]+1
print(dic1)
                
            
    
    



