# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:46:39 2022

@author: jomg0
"""
num_case = int(input())
count = 0
sum = 0
for i in range(num_case):
    ox = input()
    for j in ox:
        if j =='O':
           count = count+1
           sum = sum+count
        elif j =='X':
            count= 0
    print(sum)
    
    sum = 0
    count = 0