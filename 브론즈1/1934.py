def gcd(a,b):
    while(b!=0):
        temp = a % b 
        a = b
        b = temp
    return a

def lcm(a,b):
    G = gcd(a,b)
    print(a*b//G)



test_case = int(input())

for _ in range(test_case):
    a , b = map(int, input().split())

    lcm(a,b)