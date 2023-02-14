# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:36:39 2022

@author: jomg0
"""
x= int(input())
num = [x]
num = input().split()
max = int(num[0])
min = int(num[0])

for i in num[1:]:
    if int(i)>max:
        max=int(i)
    if int(i)<min:
        min = int(i)
        
print(min, max)
    