import sys
input = sys.stdin.readline

num = int(input())
people = []
cnt = [0] * num
for _ in range(num) :
    w , h = map(int, input().split()) 
    people.append([w,h])
for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")
# for i in range(num):
#     weight = people[i][0]
#     height = people[i][1]
#     for j in range(num):
#         if weight > people[j][0] and height > people[j][1] : 
#             cnt[i] += 1
# sort_cnt = sorted(cnt, reverse= True)
# result = ''.join(str(s) for s in sort_cnt)
# result_li = []
# for i in cnt:
#     i = str(i)
#     result_li.append(result.find(i)+1)
# print(*result_li)