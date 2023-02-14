import sys
n , k = map(int, input().split())

line = []
for _ in range(n):
    line.append(int(sys.stdin.readline()))


start = 1
end = max(line)


while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in line:
        cnt += (i // mid)

    if cnt > k :
        start = mid + 1
    
    else:
        end = mid - 1

print(start)
