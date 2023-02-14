import sys
num = int(input())

for i in range(num):
    if i == 0:
        result = list(sys.stdin.readline().rstrip('\n'))
        length = len(result)

    else:
        temp = list(sys.stdin.readline().rstrip('\n'))
        for i in range(length):
            if result[i] != temp[i]:
                result[i] = '?'

for i in result:
    print(i, end = "")

