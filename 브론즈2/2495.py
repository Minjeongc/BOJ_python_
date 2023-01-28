for _ in range(3):
    num = input()
    cnt = 0
    for i in range(7):
        if num[i] == num[i+1]:
            cnt += 1

    