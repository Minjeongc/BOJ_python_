import math

n = int(input())
num = list(map(int, input().split()))

min_num = math.gcd(num[0], math.gcd(num[1], num[-1]))

for i in range(1,min_num//2 +1):
    if min_num % i == 0:
        print(i)

print(min_num)