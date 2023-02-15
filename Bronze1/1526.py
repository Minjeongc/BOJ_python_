n = int(input())

for i in range(n,3,-1):
    cnt = 0
    j = str(i)
    for x in j:
        if x == '4':
            cnt += 1
        elif x == '7':
            cnt += 1
    if cnt == len(j):
        print(j)
        break
    
    