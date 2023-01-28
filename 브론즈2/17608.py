import sys
n = int(input())
arr = []
for i in range(n):
    x = sys.stdin.readline().rstrip('\n')
    arr.append(int(x))
cnt = 0
max = 0

for i in reversed(arr):
    if i > max:
        max = i
        cnt +=1

print(cnt)
