n = int(input())

num = list(map(int, input().split()))
result = 0 

for i in num:
    flag = True
    if i == 1:
        flag = False
    for j in range(2,i//2+1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        result += 1 

print(result)
