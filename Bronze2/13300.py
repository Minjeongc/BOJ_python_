#학생 수: N, 최대 배정 인원 : k
N , k = map(int, input().split()) 

cnt = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
result = 0
for i in range(N):
    sex , grade  = map(int, input().split())
    cnt[sex][grade - 1] += 1

for i in cnt :
    for j in i:
        if j % k == 0:
            result += j//k
        else:
            result += (j//k) + 1
print(result)

# cnt = [[1,2,3,4,5,6],[7,8,9,10,20,30]]
# print (cnt[0][1])
# print (cnt[1][0])
