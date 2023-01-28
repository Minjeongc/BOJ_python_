# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:46:56 2022

@author: jomg0
"""
num = []

num = [int(input()) for _ in range(9)] #엔터쳐서 값 입력받기
    

max = num[0]
address = 0
for j in num[1:]:
    if j >max:
        max = j
        address = num.index(j)
    
        
print(max)
print(address+1)