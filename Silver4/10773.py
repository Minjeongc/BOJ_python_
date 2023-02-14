import sys

n = int(sys.stdin.readline())

result = []
sum = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        result.pop()
    else:
        result.append(num)

for i in result:
    sum += i

print(sum)