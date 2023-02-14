# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:58:05 2022

@author: jomg0
"""

while (1):
    try:
        x ,y = input().split()
        x = int(x)
        y = int(y)
        print(x+y)
    except:
        break