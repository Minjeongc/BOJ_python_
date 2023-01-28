# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:12:45 2022

@author: jomg0
"""


a = int(input())
num = input()
int_num = list()
sum = 0
for i in num:
    i = int(i)
    int_num.append(i)
    
    
for j in int_num:
    sum= sum+j
    
print(sum)
    