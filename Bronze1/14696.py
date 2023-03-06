import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.remove(a[0])
    b.remove(b[0])

    a_li = [0] * 4
    b_li = [0] * 4

    for i in a:
        a_li[i-1] += 1
    for i in b:
        b_li[i-1] += 1

    for i in range(3,-1,-1):
        if a_li[i] > b_li[i] :
            print("A")
            break
        elif a_li[i] < b_li[i]:
            print("B")
            break
    else:
        print("D")