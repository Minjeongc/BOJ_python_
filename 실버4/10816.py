n = int(input())
num1 = list(map(int, input().split()))
num1.sort()
m = int(input())
num2 = list(map(int, input().split()))

cnt = {}
for i in num1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in num2:
    if i in cnt:
        print(cnt[i] , '',end = '')
    else:
        print(0,'', end = '')

#dic에 대해서 공부하기 


