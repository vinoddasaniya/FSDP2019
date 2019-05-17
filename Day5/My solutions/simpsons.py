# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:59:51 2019

@author: kk
"""
 
"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""


import re
with open("simpsons_phone_book.txt", "rt") as file1:
    for i in file1:
        if re.search(r'^J[a-zA-Z]*\sNeu', i):
            print(i)