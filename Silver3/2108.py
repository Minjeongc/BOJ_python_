import sys
from collections import Counter

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    n = []

    for _ in range(num):
        n.append(int(sys.stdin.readline()))
    n.sort()
    cnt = Counter(n).most_common(2)
    print(round(sum(n)/len(n)))
    print(n[num//2])
    if len(n) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])
    print(max(n) - min(n))
