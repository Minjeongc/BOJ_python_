import sys

alpha = [0]*26

word = sys.stdin.read().replace("\n","").replace(" ","")
for i in word:
    if i.islower():
        temp = ord(i) - 97
        alpha[temp] += 1

for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(i+97), end= "")