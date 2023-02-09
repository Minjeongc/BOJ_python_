from collections import deque
num = int(input())
card = deque([])

for i in range(num) : 
    card.append(i+1)

while len(card) >1:
    print(card.popleft() ,'', end = '')
    card.append(card[0])
    card.popleft()
print(card[0], end = '')