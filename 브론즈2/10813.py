m , n = map(int,input().split())

ball = []

for i in range(m):
    ball.append(i+1)

for i in range(n):
    c1, c2 = map(int, input().split())
    temp = ball[c1-1]
    ball[c1-1] = ball[c2-1]
    ball[c2-1] = temp
print(*ball)
    
