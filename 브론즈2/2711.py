import sys
num = int(input())

for i in range(num):
    arr = []
    n , s = sys.stdin.readline().rstrip('\n').split()
    n = int(n) - 1

    for j in range(len(s)):
        if j == n:
            continue
        else:
            arr.append(s[j])

    for k in arr:
        print(k, end = "")
    print("")


