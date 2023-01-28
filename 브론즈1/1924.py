x , y = map(int, input().split())


# 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28
#1:월, 2:화, 3:수, 4:목, 5: 금, 6: 토, 0: 일
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

cnt = 0

for i in range(1, x):
    if i == 4 or i == 6 or i == 9 or i == 11:
        cnt += 30
    elif i == 2:
        cnt += 28
    else:
        cnt += 31
cnt += y

print(date[cnt%7])