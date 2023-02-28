test_case = int(input())

for _ in range(test_case):
    n , m = map(int, input().split())
    ans = 0
    for i in range(n , m+1):
        j = str(i)
        ans += j.count('0')
    print(ans) 