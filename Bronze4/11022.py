# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:19:16 2022

@author: jomg0
"""


T = int(input())
for j in range(T):
    x,y= input().split()
    x = int(x)
    y = int (y)
    print("Case #%d: %d + %d = %d"%(j+1,x,y,x+y))