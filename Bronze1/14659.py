n = int(input())

bow = list(map(int, input().split()))
max_bow = 0 
cnt = 0
max_cnt = 0
for i in range(n):
    if max_bow < bow[i]:
        max_bow = bow[i]
        cnt = 0
    else:
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)