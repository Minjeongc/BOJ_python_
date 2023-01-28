import sys

n = int(input())
num = []
for _ in range(n):
    num.append(sys.stdin.readline().rstrip('\n'))

num.sort()

for i in num:
    print(i)

