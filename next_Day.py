# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def next_Day(year, month, date):
    if date<=29:
        return year, month, int(date)+1
    else:
        return year, int(month)+1, 1
        
year, month, day=next_Day(1997, 10, 1)

