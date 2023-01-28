# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:25:43 2022

@author: jomg0
"""

h,m = map(int, input().split())

if m>=45:
    print(h, m-45)
else:
    if h==0 and m<45:
        h = 23
        m =15+m
        print(h,m)
    else:
        print(h-1, 15+m)
        