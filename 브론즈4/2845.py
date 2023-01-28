num,area = input().split()
num = int(num)
area = int(area)
a = 0

arr = list(map(int,input().split()))
output = []

for i in arr:
    a = i-(num*area)
    output.append(a)

for j in output:
    print(j, end= " ")