# import sys
# from math import sqrt
# while True:
#     num = int(sys.stdin.readline())
    
#     if num == 0:
#         break
#     cnt = 0
#     for i in range(num+1, 2*num + 1):
#         if i == 1:
#             continue
#         elif i == 2:
#             cnt += 1
#             continue
#         for j in range(2,int(sqrt(i))+1):
#             if i % j == 0:
#                 break
#         else:
#             cnt += 1
            
#     print(cnt)
# from math import sqrt 
# def search (x):
#     if x == 1:
#         return False 
#     for i in range(2, int(sqrt(i))+1):
#         if x % i == 0 :
#             return False
#     return True
# num = list(range(2,246912))
# r = []
# for x in num:
#     if search(x):
#         r.append(x)

# n = int(input())

# while True:
#     cnt = 0
#     if n == 0:
#         break
#     for i in r:
#         if n < i <= 2*n:
#             cnt += 1
#     print(cnt)
#     n = int(input())


def search_num(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							

n_list = list(range(2,246912))		
num = []								
for i in n_list:						
    if search_num(i):							
        num.append(i)					

n = int(input())

while True:
    cnt=0					
    if n == 0 :
            break
    for i in num:			
        if n < i <=2*n:		
            cnt+=1		
    print(cnt)
    n = int(input())	