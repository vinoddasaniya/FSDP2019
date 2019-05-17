# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:53:43 2019

@author: kk
"""

#    Write a Python program to construct the following pattern. 


rows = input("Input")
rows = int (rows)
print("Output")
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*",end=' ')
    print("\r")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")