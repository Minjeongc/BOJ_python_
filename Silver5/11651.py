import sys
testCase = int(input())
li = []
for _ in range(testCase):
    x ,y = map(int, sys.stdin.readline().split())
    li.append([y,x])

# li.sort(key = lambda a  : (a[-1], a[0]))

# for i in li:
#     for j in i:
#         print(j , end = " ")
#     print("")
s_li = sorted(li)
for y,x in s_li:
    print(x,y)

# 시간초과: input()
