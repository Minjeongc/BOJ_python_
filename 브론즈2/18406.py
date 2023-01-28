num = list(input())

length = len(num) //2
sum1 = 0
sum2 = 0

for i in range(length):
    sum1 += int(num[i])
for i in range(length, len(num)):
    sum2 += int(num[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")