import sys
import math
testCase = int(input())

for _ in range(testCase):
    r, n = map(int, sys.stdin.readline().split())
    print(math.comb(n,r))
