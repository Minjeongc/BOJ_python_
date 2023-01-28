name = input()

result = []
for i in name:
    j = ord(i)
    if j >= 65 and j <= 90:
        result.append(i)

for k in result:
    print(k, end = "")