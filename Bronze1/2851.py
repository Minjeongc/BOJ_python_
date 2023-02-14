import sys

score = 0
num = []

for _ in range(10):
    num.append(int(sys.stdin.readline()))

for i in range(10):
    score += num[i]

    if score >= 100:
        temp = i
        break

s1 = score
s2 = score - num[i]

if score == 100:
    print(score)
elif abs(s1-100) <= abs(s2-100):
    print(s1)
else :
    print(s2)
