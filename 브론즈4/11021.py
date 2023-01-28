# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:09:12 2022

@author: jomg0
"""

i = int(input())

for j in range(i):
    x,y= input().split()
    x = int(x)
    y = int (y)
    print("Case # %d: %d"%(j+1,x+y))