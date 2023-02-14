#최대사람인원

num = int(input())
seat = input()
cnt = seat.count('LL')

if cnt == 0 :
    print(num)
elif cnt == 1:
    print(num)
else:
    print(num - cnt + 1)