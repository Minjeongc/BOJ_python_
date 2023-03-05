import sys


num = int(sys.stdin.readline())
result = 0

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = sorted(b)

a.sort(reverse = True)

for i in range(num):
    result += (a[i]*c[i])

print(result)
    