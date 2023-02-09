tree = list(map(int, input().split()))

# 1-2 / 2-3 / 3-4 / 4-5
i = 0
j = 1
result = 0
while True:
    if result == 4:
        break
    if j == 5:
        i = 0
        j = 1
    if tree[i] > tree[j]:
        result = 0
        temp = tree[i]
        tree[i] = tree[j]
        tree[j] = temp
        print(*tree)
        i += 1
        j += 1
    else:
        result += 1
        i += 1
        j += 1

    