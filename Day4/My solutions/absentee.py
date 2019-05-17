# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:24:38 2019

@author: kk
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

fp=open("absentee1.txt","w")
fp.close()

with open("absentee1.txt", "a") as fp:
    n=0
    while n<25:
        a = input('Enter Student Name')
        z=fp.write(a + "\n")
        n=n+1
        if not a:
            break  

z=open("absentee1.txt","r")
z.read() 
    

 #"""""""""""""""""""""""""""""""""""""""""""" 


fp=open("absentee.txt","w")
fp.close()

with open("absentee.txt","a") as ab:
    for i in range(25):
        text=input("enter the name of the student   :")
        if not text:
            break
        ab.write(text + "/n")

z=open("absentee.txt","r")
z.readlines() 
    
