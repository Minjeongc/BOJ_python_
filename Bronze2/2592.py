import sys

arr = []
avg = 0
#mode 
cnt = 0
mode = 0

for i in range(10):
    x = sys.stdin.readline().rstrip('\n')
    arr.append(int(x))

for i in arr:
    avg += i
avg = avg // 10

for i in arr:
    temp = arr.count(i)
    if temp > cnt :
        cnt = temp
        mode = i

    


print(avg)
print(mode)



