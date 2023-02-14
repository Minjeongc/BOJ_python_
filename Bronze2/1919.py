word1 = input()
word2 = input()

result=0

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i]!=" " and word1[i] == word2[j]:
            word = word1[i]
            word1 = word1.replace(word1[i], " ", 1)
            word2 = word2.replace(word2[j], " ", 1)
            break

for i in range(len(word1)):
    if word1[i]!=' ':
        result +=1

for i in range(len(word2)):
    if word2[i]!=' ':
        result +=1

print(result)
