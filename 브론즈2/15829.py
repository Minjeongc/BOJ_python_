import math
# a= 1,..., z= 26

num = int(input())
result = 0
cnt = 0

hash = input()

for i in hash:
    x = ord(i) - 96
    temp = x * (pow(31,cnt))
    result += temp
    cnt += 1
    
print(result%1234567891)