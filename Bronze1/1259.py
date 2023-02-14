import sys
while (True):
    num = sys.stdin.readline().rstrip('\n')
    cnt = 0
    length = len(num)
    if num == '0':
        exit()
    for i in range(length//2):
        num1 = int(num[i])
        num2= int(num[length-1-i])
        if num1!= num2:
            print("no")
            cnt = 1
            break
    if cnt != 1 :
        print("yes")
