num = int(input())

score = list(map(int, input().split()))

score.sort()

print(score[num-1] - score[0])