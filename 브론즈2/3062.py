import sys

test_case = int(sys.stdin.readline().rstrip('/n'))

for _ in range(test_case):
    num = sys.stdin.readline().rstrip('/n')
    temp = ''
    for i in reversed(num):
        temp += i
    
    result = str(int(num) + int(temp))

    flag = True
    for i in range(len(result)//2):
        if result[i] != result[-1-i]:
            flag = False
            break
    if flag == False:
        print('NO')
    else:
        print('YES')
    
