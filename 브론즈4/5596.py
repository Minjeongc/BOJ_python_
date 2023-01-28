a = []
score = []

for i in range (2):
    amount = 0
    score = map(int,input().split())
    for j in score:
        amount += j
    a.append(amount)

if a[0] < a[1]:
    print(a[1])
else:
    print(a[0])
