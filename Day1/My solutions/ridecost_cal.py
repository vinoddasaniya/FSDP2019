# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:49:32 2019

@author: kk
"""

#Assume you travel 80 km to and fro in a day. 
#Cost of Diesel per litre is 80 INR 
#Your vehicle Fuel Average is 18 km/litre. 
#Now calculate the cost of driving per day to office. 


travel = 160
Diesel_cost = 80
vehicle_average = 18

total_used_fuel = travel / vehicle_average
cost_of_driving_per_day = total_used_fuel * Diesel_cost
print(cost_of_driving_per_day)