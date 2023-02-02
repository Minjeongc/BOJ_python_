# 시간초과
# import sys

# num = int(sys.stdin.readline())

# queue = []

# for _ in range(num):
#     command = sys.stdin.readline().split()

#     if command[0] == 'push':
#         queue.append(command[1])
        
#     elif command[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.pop(0))
    
#     elif command[0] == 'size':
#         print(len(queue))
        
#     elif command[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)

#     elif command[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])

#     elif command[0] == 'back':
#         if len(queue) == 0 :
#             print(-1)
#         else:
#             print(queue[-1])

#시간초과 X  => deque 사용

import sys
from collections import deque
num = int(sys.stdin.readline())

queue = deque([])

for _ in range(num):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command[0] == 'back':
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[-1])

# deque에 대해 정리하기.
