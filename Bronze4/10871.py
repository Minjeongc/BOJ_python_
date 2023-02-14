# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:07:25 2022

@author: jomg0
"""
x,y= input().split()
x = int(x)
y = int(y)
z = [100000]
z = input().split()

for i in range(0,x):
    z[i]= int(z[i])
    
for j in range(0,x):
    if z[j]<y:
        print(z[j])
        
        