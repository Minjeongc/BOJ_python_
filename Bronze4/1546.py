# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:28:27 2022

@author: jomg0
"""

subject = int(input())

aver = [subject]

aver= map(int,input().split())

aver = list(aver)

max_aver= [subject]

sum = 0

max= aver[0]

for i in aver[1:]:
    if i > max:
        max = i #최대값구하기
        
for j in aver:
    j = j / max*100
    sum = sum + j
    
    
print(sum/subject)