# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:07:02 2022

@author: jomg0
"""
 
a,b = map(int,input().split()) #두수를 입력받아 나누는 방법


if a>b:
    print(">")
elif a<b:   
    print("<")
else:
    print("==")
