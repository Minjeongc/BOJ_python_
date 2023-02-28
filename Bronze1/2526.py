n , p = map(int, input().split())

temp = 1
ans = []
while True:
    temp = (temp * n) % p
    if temp in ans:
        print((len(ans)) - ans.index(temp))
        break
    ans.append(temp)

# 처음 이용한 방법은 반복되는 부분에서의 서로다른 개수를 출력하는 것이 아니라 그냥 서로 다른 temp의 값을 출력하는 방법임. 
