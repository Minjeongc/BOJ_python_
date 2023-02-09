import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))


def Search(target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target :
            return True
        if target >  n_list[mid] :
            start = mid + 1
        elif target < n_list[mid]  :
            end  = mid - 1

for i in range(m):
    if Search(m_list[i]):
        print(1 ,'', end = '')
    else:
        print(0,'', end = '')