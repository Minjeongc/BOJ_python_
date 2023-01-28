a,b,c = map(int, input().split())


car1 = list(map(int, input().split()))
car2 = list(map(int, input().split()))
car3 = list(map(int, input().split()))

result = 0

min_arr = min(car1[0], car2[0], car3[0])
max_leave = max(car1[1], car2[1], car3[1])


for i in range(min_arr, max_leave+1):
    cnt = 0
    if i in range(car1[0], car1[1]) :
         cnt += 1
    if i in range(car2[0], car2[1]) :
         cnt += 1
    if i in range(car3[0], car3[1]) :
         cnt += 1    

    if cnt == 1:
        result += a
    elif cnt == 2:
        result += b*2
    elif cnt == 3:
        result += c*3


print(result)
