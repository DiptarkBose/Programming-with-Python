# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

print nextDay(1997, 10, 11)