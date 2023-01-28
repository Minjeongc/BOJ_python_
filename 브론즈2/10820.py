import sys 

while True : 
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break

    arr = [0,0,0,0]

    for i in line:
        if i.islower():
            arr[0] += 1
        elif i.isupper():
            arr[1] += 1
        elif i.isdigit():
            arr[2] += 1
        elif i.isspace():
            arr[3] += 1
    print(arr[0], arr[1], arr[2] , arr[3])