n = int(input())

temp = 2

while (n >1):
    if n % temp == 0:
        print(temp)
        n = n//temp
    else:
        temp +=1
