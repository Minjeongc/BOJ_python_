n , m = map(int, input().split())
castle = []
guard = []
for i in range(n):
    temp = input()
    castle.append(temp)
    for j in range(len(temp)):
        if temp[j] == 'X':
            guard.append([i,j])
c = set()
r = set()
for i in guard:
    c.add(i[0])
    r.add(i[1])

temp1 = n - len(c)
temp2 = m - len(r)
print(max(temp1, temp2))