import sys
n = int(input())
result = []

p = list(map(int, sys.stdin.readline().split()))

p.sort()

for i in range(n):
    result.append(sum(p[:i+1]))

print(sum(result))

# 정렬 sort함수 대신 다시 구현해보기
