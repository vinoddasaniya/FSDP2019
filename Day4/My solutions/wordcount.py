# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:24:26 2019

@author: kk
"""


"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
file_name = raw_input ("Enter File Name: ")

no_of_character=0
no_of_words=0
no_of_unique_words=0
for no_of_lines, line in enumerate (open(file_name), 1):
    no_of_character += len(line)
    no_of_words += len(line.split())
    no_of_unique_words
    
    
print("no of lines: ", format(no_of_lines))    
print("no of characters: ", format(no_of_character) ) 
print("no of words: ", format(no_of_words) )    
print("no of unique words: " ) 
