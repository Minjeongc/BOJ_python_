length  = int(input())

num = list(map(int, input().split()))

result = []
for i in range(length):
    temp = num[i] * (i+1)
    for j in range(i):
        temp -= result[j]
    result.append(temp)
    
        


print(*result)