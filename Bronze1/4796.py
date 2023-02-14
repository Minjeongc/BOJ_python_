import sys

case = 1
while True:
    l, p , v = map(int, sys.stdin.readline().split())
    if l+p+v == 0:
        break

    cnt = (v//p)*l
    cnt += min((v%p),l) 

    print('Case %d: %d'  %(case, cnt))

    case += 1

