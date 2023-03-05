import sys
n , m = map(int, sys.stdin.readline().split())

see = set()
hear = set()
for _ in range(n):
    hear.add(sys.stdin.readline().rstrip('\n'))

for _ in range(m):
    see.add(sys.stdin.readline().rstrip('\n'))

arr = sorted(list(see & hear))
print(len(arr))

for i in arr:
    print(i)

# set에 대해서 더 공부하기. 
