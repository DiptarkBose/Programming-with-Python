# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 10:06:22 2017

@author: Diptark Bose
"""

def sum_list(list):
    sum=0    
    for elem in list:
        sum=sum+elem
    return sum
        
p=[1, 2, 3, 4]
print sum_list(p)