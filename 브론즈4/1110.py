# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:06:47 2022

@author: jomg0
"""
z= int(input())
x = z // 10 #10의자리
y = z % 10  #1의자리
sum_num = x+y #합한숫자
new_num = (z%10)*10 + sum_num%10
count = 1
while new_num!=z:
    x = new_num // 10 #10의자리
    y = new_num % 10  #1의자리
    sum_num = x+y #합한숫자
    new_num = (new_num%10)*10 + sum_num%10
    count = count+1

print(count)