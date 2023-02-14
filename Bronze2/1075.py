#첫번째코드

N = int(input())
F = int(input())

r = N%F

num = N%100 

if r == 0:
    print('00')

else:
    if num >= r:
        result = N - r
    else:
        result = N +(F-r)

while (result%100) >= F :
    result = result - F 

if result % 100 == 0:
    print('00')
else:
    print(result%100)