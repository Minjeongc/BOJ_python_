# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:22:10 2022

@author: jomg0
"""

num = []
count = [0,0,0,0,0,0,0,0,0,0]

num = [int(input()) for _ in range(3)] #엔터쳐서 값 입력받기
    

mul = str(num[0]*num[1]*num[2])

for i in mul:
    if i =='0':
        count[0] = count[0]+1
    elif i =='1':
        count[1] = count[1]+1
    elif i =='2':
        count[2] = count[2]+1 
    elif i =='3':
        count[3] = count[3]+1
    elif i =='4':
        count[4] = count[4]+1
    elif i =='5':
        count[5] = count[5]+1
    elif i =='6':
        count[6] = count[6]+1
    elif i =='7':
        count[7] = count[7]+1
    elif i =='8':
        count[8] = count[8]+1
    elif i =='9':
        count[9] = count[9]+1
        
for j in count:
    print(j)