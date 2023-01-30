
num = int(input())

li = []
for _ in range(num):
    age, name = map(str, input().split())
    age = int(age)
    li.append([age, name])

li.sort(key = lambda li : li[0])

for i in li:
    for j in i:
        print(j, end = " ")
    print()