num = list(map(int, input().split()))

max = 0
min = 0
mid = 0
for i in range(3):
    if num[i] > max:
        min = mid
        mid = max
        max = num[i]

    else:
        if num[i] < mid:
            min = num[i]
            
        else:
            min = mid
            mid = num[i]
print(min, mid, max)