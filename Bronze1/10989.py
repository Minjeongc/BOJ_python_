# 메모리초과: 정렬방법과 관련없음. 
# append 함수와 관련있음.
# 계수정렬 
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num = [0] * 10001

    for i in range(n) : 
        a = int(sys.stdin.readline())
        num[a-1] += 1
    for i in range(10001):
        if num[i] != 0:
            for j in range(num[i]):
                print(i+1)
