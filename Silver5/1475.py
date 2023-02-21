import math 
n = input()
li = [0]*9
n = n.replace('9','6')

for i in n:
    j = int(i)
    li[j] += 1
li[6] = math.ceil(li[6] / 2)
print(max(li))