num = list(map(int, input().split()))

max = max(num[0],num[1],num[2])
min = min(num[0],num[1],num[2])
mid = 0

for i in num:
    if i != max and i != min:
        mid = i


print(min, mid, max)