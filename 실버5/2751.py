import sys

test_case = int(input())
num = []
for _ in range(test_case):
    num.append(int(sys.stdin.readline().rstrip('\n')))

num.sort()

for i in num:
    if i != " ":
        print(i)