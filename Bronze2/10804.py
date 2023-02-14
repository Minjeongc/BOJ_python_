card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(10):
    minNum, maxNum = map(int, input().split())
    cnt = maxNum - minNum 
    if cnt%2 == 0:
        cnt = cnt //2
    else:
        cnt = (cnt //2 ) +1
    for i in range(cnt):
        temp = card[minNum-1+i]
        card[minNum-1+i] = card[maxNum-1-i]
        card[maxNum-1-i] = temp
for j in card:
    print(j,"", end = "")





 

