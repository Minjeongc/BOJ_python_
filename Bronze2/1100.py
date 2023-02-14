
cnt = 0

for i in range (8):
    arr = input()
    for j in range(8):
        if ((i+j)%2 == 0) and (arr[j] == 'F'):
            cnt = cnt+1

print(cnt)
