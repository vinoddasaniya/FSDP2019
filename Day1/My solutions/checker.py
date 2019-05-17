# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:05:52 2019

@author: kk
"""

#    Print the checkerboard pattern using escape Codes and Unicode 
#    with multiple print statements and the multiplication operator 

x = ' *'
x1 = x * 8
y = '  *'
y1 = y * 8
i=0
while i <10:
    list1 = [0,2,4,6,8,10]
    if i in list1:
        print(x1)
    else:
        print(y1)
    i+=1
        
        
    