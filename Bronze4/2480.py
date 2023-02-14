S = list(map(int, input().split()))
S.append(S[0])

count = 0
max = 0

for i in range(3):
    if S[i] == S[i+1]:
        count +=1
        same = S[i]
if count ==0:
    for i in S:
        if max < i:
            max = i
    print(max*100)
elif count == 1:
    print(same*100 + 1000)

elif count == 3:
    print(same*1000 + 10000)