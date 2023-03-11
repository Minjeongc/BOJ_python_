import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for _ in range(n):
    site , pw = map(str, input().split())
    dict[site] = pw

for _ in range(m):
    search = input().rstrip()
    print(dict[search])        