# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:35:38 2017

@author: Diptark Bose
"""
def measure_udacity(list):
    count=0    
    for elem in list:
        if elem[0]=='U':
            count=count+1
    return count
    
print measure_udacity(['Umika','Umberto'])
