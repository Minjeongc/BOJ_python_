test_case = int(input())

for _ in range(test_case) : 
    distance = []
    word1, word2 = map(str, input().split())
    for i in range(len(word1)):
        temp1 = ord(word1[i]) - 64
        temp2 = ord(word2[i]) - 64

        if temp1 <= temp2:
            distance.append(temp2-temp1)
        else:
            distance.append(temp2+26-temp1)
    print("Distances:", *distance)