n = int(input())
seq = []

for i in range(n):
    mid = input()
    seq.append(mid)

for j in range(n):
    print(j+1, ". ",seq[j],sep = "",)