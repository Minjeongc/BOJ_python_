# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:23:41 2022

@author: jomg0
"""

x=int(input())
y=int(input())

if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
else:
    print("4")