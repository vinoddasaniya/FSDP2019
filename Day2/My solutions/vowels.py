# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:29:55 2019

@author: kk
"""

# Remove all the vowels from the list of states  


state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
def anti_vowel(state_name):
    newstr = state_name.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in newstr:
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr
    print(x)
    
    
