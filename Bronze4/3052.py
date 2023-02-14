# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:31:12 2022

@author: jomg0
"""

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

