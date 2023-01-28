dwarf = []
sum = 0

for i in range(9):
    dwarf.append(int(input()))


for j in dwarf:
    sum += j

num = sum - 100

for i in range(9):
    for j in range(i+1,9):
        if num == (dwarf[i] + dwarf[j]):
            a = i
            b = j
dwarf.pop(a)
dwarf.pop(b-1)

for k in dwarf:
    print(k)