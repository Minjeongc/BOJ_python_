# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:15:24 2022

@author: jomg0
"""

num = int(input())
count = 0

def aver(case_list, case_num):
    sum = 0
    for i in case_list[1:]:
        sum = sum + i
    ava = sum/case_num
    return ava
    
def cal():
   case_list = map(int,input().split())
   case_list= list(case_list)
   ava= aver(case_list, case_list[0])
   count = 0
   for j in case_list[1:]:
       if j> ava:
           count = count+1
   result = (count/ case_list[0]) * 100
    
   print("%0.3f%%" % result)    

for i in range(num):
    cal()



