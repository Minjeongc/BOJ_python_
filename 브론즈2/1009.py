case = int(input())

#시간초과
#for i in range(case):
#    a,b = map(int, input().split())
#
#    print((a**b)%10)
for i in range(case):
    a,b = map(int, input().split())

    c = a%10 #a의 일의자리 

    if c==0:
        print(10)
    elif c in [1,5,6]:
        print(c)

    elif c in [4,9]:
        if b%2==1:
            print(c)
        else:
            print((c*c)%10)

    else:
        d = b%4
        if d==0:
            print(c)
        else:
            print((c**d)%10)

