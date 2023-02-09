from math import sqrt
def thtn(x):
    if x == 2:
        return True
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True
        
test_case = int(input())
for _ in range(test_case):
    result = []
    num = int(input())
    for i in range(2, num//2+1):
        a = i
        b = num - i
        if thtn(a) and thtn(b):
            result.append([a,b])
    #result.sort(key = lambda x :x[0])
    print(result[-1][0], result[-1][1])
