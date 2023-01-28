num = int(input())

for _ in range(num):
    li = list(input().split())
    for word in li:
        for j in reversed(word):
            print(j, end = "")
        print(end = " ")
