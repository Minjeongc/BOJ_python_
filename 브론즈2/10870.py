from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n== 0:
        return 0
    elif (n==1 or n==2):
        return 1
    else :
        return fib(n-1)+fib(n-2)

if __name__ == "__main__" :
    n  = int(input())
    print(fib(n))

##memorization: 이전에 계산한 값을 저장해서 중복된 계산을 피하는 방법.
##재귀함수의 경우 시간복잡도를 줄여 성능을 향상시킬 수 있음.