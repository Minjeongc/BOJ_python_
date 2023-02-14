i = input()
j = i.upper()
max = 0 
count = 0

num = [0]*26 
for k in j:
    m = ord(k)
    num[m-65] +=1 

print(num)

for l in num: 
    if max < l :
        max = l 
        a = num.index(max)

for g in num : 
    if num(a) == g:
        count += 1  
if count>=2:
    print("?")
else :
    print(chr(a+65))


