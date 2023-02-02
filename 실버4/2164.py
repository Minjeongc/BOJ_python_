import sys 
from collections import deque
num = int(sys.stdin.readline())

result = deque([])

for i in range(num):
    result.append(i+1)

while len(result) > 1:
    result.popleft()
    temp = result[0]
    result.popleft()
    result.append(temp)
print(result[0])


#deque로 스택과 큐 모두 구현 가능함. 
