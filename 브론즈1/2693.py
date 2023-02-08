test_case = int(input())

for _ in range(test_case):
    num = list(map(int,input().split()))
    num.sort()

    print(num[-3])

    