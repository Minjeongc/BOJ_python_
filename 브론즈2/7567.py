bowl = input()

height = 10

for i in range(len(bowl)-1):

    if bowl[i] == bowl[i+1]:
        height += 5
    else:
        height += 10

print(height)
