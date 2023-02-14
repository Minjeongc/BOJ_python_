M = int(input())
N = int(input())
num = []
num_add = 0
i = 1
while i ** 2 <= N:
    if M <= i ** 2 <= N:
        num.append(i ** 2)
        num_add += i**2
    i += 1

if num_add == 0 :
    print(-1)
else:
    print(num_add)
    print(num[0])