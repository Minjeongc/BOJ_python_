num = int(input())

c = []
for _ in range(num):
    x,y = map(int, input().split())
    c.append([x,y])
    
c.sort(key = lambda c : (c[0], c[1]))


for i in c:
    for j in i:
        print(j, end = " ")
    print()