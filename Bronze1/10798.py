word = []
max_length = 0
for i in range(5):
    temp = input()
    word.append(temp)
    if len(temp)> max_length:
        max_length = len(temp)
for i in range(5):
    if len(word[i]) < max_length:
        for j in range(max_length - len(word[i])):
            word[i] =  word[i]+'.'

for i in range(max_length):
    for j in range(5):
        if (word[j][i]) != ".":
            print(word[j][i], end = "")

