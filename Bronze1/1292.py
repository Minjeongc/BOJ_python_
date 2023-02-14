m, n = map(int , input().split())

result = []
for i in range(1,n+1):
    for j in range(i):
        result.append(i)


print(sum(result[m-1:n]))