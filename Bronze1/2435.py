import sys
input = sys.stdin.readline

num , length = map(int, input().split())

temp = list(map(int, input().split()))

for i in range(num-length+1):
    sum = 0
    for j in range(i, i+length):
        sum += temp[j]
    if i == 0:
        max = sum
    elif max < sum:
        max = sum
    
print(max)
