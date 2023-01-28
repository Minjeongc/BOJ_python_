num = int(input())

for _ in range(num):
    referee = list(map(int, input().split()))
    referee.remove(max(referee))
    referee.remove(min(referee))

    if max(referee) - min (referee) >= 4:
        print("KIN")
    else:
        print(sum(referee))