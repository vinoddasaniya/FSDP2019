# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:45:59 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""



fp = open("words.txt", "rt")
x = fp.read()
gp = open("words2.text", "wt")
gp.write(x)
gp.close()
fp.close()

