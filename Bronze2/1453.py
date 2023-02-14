n = int(input())
arr = list(map(int, input().split()))
seat = []
refuse = 0


for i in arr:
    if seat.count(i) == 0:
        seat.append(i)
    else:
        refuse += 1

print(refuse)