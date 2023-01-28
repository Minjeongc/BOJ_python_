time = []
amo = 0

for i in range(4):
    sec = int(input())
    time.append(sec)

for j in time:
    amo += j

print(amo // 60)
print(amo % 60)