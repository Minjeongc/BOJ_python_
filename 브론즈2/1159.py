import sys
N = int(input())

alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
result = []
#97~122 

for i in range(N):
    name = input()
    for j in range(26):
        if ord(name[0]) == j+ 97:
            alpha[j] += 1
            

for i in range(26):
    if alpha[i]>=5:
        result.append(chr(i+97))

if len(result)==0:
    print("PREDAJA")
else:
    for i in result:
        print(i, end = '')

