# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:52:31 2017

@author: Diptark Bose
"""

squares=[x**2 for x in range(1, 11)]
print squares
print filter(lambda x: x>30 and x<70, squares)