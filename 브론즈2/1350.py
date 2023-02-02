import sys
num = int(input())

file_list = sys.stdin.readline().split()

cluster = int(input())

cnt = 0

for i in file_list:
    i = int(i)
    if i % cluster == 0:
        cnt += i //cluster
    else:
        cnt += (i//cluster + 1)


print(cnt*cluster)