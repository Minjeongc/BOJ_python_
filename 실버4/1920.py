n = int(input())
num1 = set(map(int, input().split()))

m = int(input())
num2 = list(map(int, input().split()))


for i in num2:
    if i in num1:
        print(1)
    else:
        print(0)

#이진탐색
n = int(input())
num1 = set(map(int, input().split()))
num1.sort()

m = int(input())
num2 = list(map(int, input().split()))


def search(target):
    start = 0
    end = n -1

    while start <= end:
        mid = (start + end) // 2
        if num1[mid] == target:
            return True
        
        if target < num1[mid]:
            end = mid - 1
        elif target > num1[mid]:
            start = mid + 1

for i in range(m):
    if search(num2[i]):
        print(1)
    else:
        print(0)