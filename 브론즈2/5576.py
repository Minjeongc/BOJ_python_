
a = list()
b = list()

result1 = 0
result2 = 0

for _ in range(10):
    a.append(int(input()))

for _ in range(10):
    b.append(int(input()))


a.sort(reverse = True)
b.sort(reverse = True)

for i in range(3):
    result1 += a[i]
    result2 += b[i]

print(result1, result2)
