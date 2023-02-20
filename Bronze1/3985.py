rollCake = int(input())
people = int(input())

piece = []
want = 0
wantPerson = 0 
temp = [0] * rollCake
real = []

for i in range(people):
    m, n = map(int, input().split())
    piece.append([m,n])
    if n-m > want:
        want = n - m
        wantPerson = i + 1

for i in range(people):
    m = piece[i][0]
    n = piece[i][1]
    for j in range(rollCake):
        if m <= j <= n:
            if temp[j] == 0 :
                temp[j] = i+1

for i in range(people):
    real.append(temp.count(i+1))
            
print(wantPerson)
print(real.index(max(real))+1)