import sys
from math import sqrt 
while(True):
    num = int(sys.stdin.readline())
    if num == -1:
        break
    dirtn = []
    #약수구하기
    for i in range(1,int(sqrt(num))+1):
        if i == 1:
            dirtn.append(i)
        elif num % i == 0:
            dirtn.append(i)
            if (i**2)  ==  num:
                continue
            else:
                dirtn.append(int(num//i))
    dirtn.sort()
    if sum(dirtn) == num:
        print(num , '= ', end = '')
        for i in dirtn:
            if i != dirtn[-1]:
                print(i, '+ ', end = '')
            else:
                print(i)
    else:
        print("%d is NOT perfect."%num)

