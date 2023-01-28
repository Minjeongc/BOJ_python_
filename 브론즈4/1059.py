# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:21:33 2022

@author: jomg0
"""
    
def sorting(S,n):
    a = S.index(n)
    b = S[a-1]
    c = S[a+1]
    d = S[a]
    sum = 0
    set_1 = set()
    
    for i in range(b+1,c):
        if i < d:
            for j in range(i+1,c):
                print(i,j)
                sum = sum + 1
        elif i> d:
            for k in range(b,i-1):
                print(k,i)
                sum = sum+1
    return sum

L = int (input())
S = list()
S = input().split()
n = int(input())
S = list(map(int,S))
S.append(n)
S.sort()
data = sorting(S,n)

print(data)





