# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:10:58 2022

@author: jomg0
"""

def sum(a):
    total = 0
    for i in a:
       total = i + total  
    return total

n = int(input())

a = [int(input()) for _ in range(n)]

total = print(sum(a))
