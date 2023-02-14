a,b = map(int, input().split())

max_num = max(a,b)
min_num = min(a,b)
if a==b:
    print(0)
else:
    print(max_num - min_num -1)

for i in range(min_num+1, max_num):
    print(i,end = ' ')
