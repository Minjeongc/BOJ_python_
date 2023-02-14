word =  list(input())
cnt = 0
for i in range(((len(word)//2)+1)):
    if word[i] != word[-1-i]:
        cnt +=1


if cnt==0:
    print(1)
else:
    print(0)
