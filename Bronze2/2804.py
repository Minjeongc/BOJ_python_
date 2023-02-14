a,b = map(str, input().split())

a = list(a)
b = list(b)

result = []

for i in a:
    if i in b :
        temp = i
        a_index = a.index(temp)
        b_index=  b.index(temp)
        break
m = len(b)
n = len(a)
for i in range(m):
    for j in range(n):
        if i != b_index:
            if j == a_index:
                print(b[i], end = "")
            else:
                print('.', end = "")
        else:
            print(a[j], end = "")

    print("")
