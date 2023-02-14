num = int(input())

car = []

count = 0

car = map(int,input().split())

for i in car:
    if i==num:
        count +=1 

print(count)