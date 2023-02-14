num = int(input())

road = list(map(int, input().split())) 
length = [0] * num
temp = 0 
for i in range(1,len(road)):
    if road[i] - road[i-1] > 0 :
        length[temp]+=(road[i] - road[i-1])
    else:
        temp += 1

print(max(length))


