# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:36:54 2022

@author: jomg0
"""

test = int(input())

def p():
    total = ''
    num, string = input().split()
    num = int(num)
    for i in string:
        for j in range(num):
            total = total + i
    return total

for i in range(test):
    total = p()
    print(total)
    
    
    