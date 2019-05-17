# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:05:22 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers
    bought on a particular day. 
    Your task is to print each item_name and net_price in order of its 
    first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
d={}
while True:
    input_items = input("Enter Item Details").split()
    
    if not input_items:
        break
    
    x = " ".join(input_items[:-1])
    y = input_items[-1]
    d[x]=d.get(x,0)+int(y)
    
    
    
print(d)    
