# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:17:41 2022

@author: jomg0
"""

year= int(input())

if (year%4==0 and year%100!=0) or year %400==0:
    print("1")
else:
    print("0")
