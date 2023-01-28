N , B = input().split()
B = int(B)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
cnt = 0

for i in (reversed(N)):
    if i in alpha:
        result += (alpha.index(i)+10)*(B**cnt) 
    else:
        result += int (i) * (B ** cnt)
    cnt += 1 

print(result )
    

