# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:14:43 2017

@author: Diptark Bose
"""

def union(list1, list2):
    new_list=list1
    for elem in list2:
        count=0
        for p in new_list:
            if elem==p:
                count=count+1
        if count==0:
            new_list.append(elem)
    return new_list
    
p1=[1, 2, 3]
p2=[2, 3, 4, 5]
print union(p1, p2)
        
    