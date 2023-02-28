test_case = int(input())

for i in range(test_case):
    score = list(map(int, input().split()))
    score.remove(score[0])
    score.sort(reverse= True)
    temp = 0
    for j in range(len(score)-1):
        if score[j] - score[j+1] > temp:
            temp = score[j] - score[j+1] 


    print("Class %d" %(i + 1))
    print("Max %d, Min %d, Largest gap %d" %(score[0], score[-1], temp))