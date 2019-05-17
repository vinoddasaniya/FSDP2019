# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:59:03 2019

@author: kk
"""

#Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
#Respective weights are 10%, 10%, 10%, 35%, 35% . 
#Compute the weighted score based on individual assignment scores.  

A1, A2, A3 = 10, 10, 10
E1, E2 = 35, 35

weighted_score = ( A1 + A2 + A3 ) * 0.1 + (E1 + E2 ) * 0.35
print (weighted_score)