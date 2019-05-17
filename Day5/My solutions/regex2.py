# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:57:51 2019

@author: kk
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
import re
while True:
    input_emails = input("Enter the email id: ")
    
    if not  input_emails:
        break
    if re.match(r'^[\w-]+@[a-z0-9]+\.[a-z]{2,4}$' ,input_emails):
        print('Valid email id')
    else:
        print('Invalid email id')
        

