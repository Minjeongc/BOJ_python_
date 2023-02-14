
a = int(input())
b = int (input())
c = int (input())
cnt = [0,0,0,0,0,0,0,0,0,0]



result = str(a*b*c)

for i in result:

    for j in range(10):
        if i == str(j):
            cnt[j] = cnt[j] +1

for k in cnt:
    print(k)

