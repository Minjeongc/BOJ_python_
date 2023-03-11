import sys

li, problem = map(int, sys.stdin.readline().split())

encyclopedia = {}

for i in range(1,li+1):
    temp = sys.stdin.readline().rstrip()
    encyclopedia[i] = temp
    encyclopedia[temp] = i 

for _ in range(problem):
    word = sys.stdin.readline().rstrip()
    if 65 <= ord(word[0]) <= 122:
        print(encyclopedia[word])
    else:
        print(encyclopedia[int(word)])