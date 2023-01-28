n , m , l = map(int, input().split())

person = [1] + [0] * (n-1)
i = 0
cnt = 0
while max(person) < m :
    
    if person[i] % 2 == 1:
        i += l
        if i >= len(person):
            i = i - len(person) 
        person[i] += 1
    else:
        i -= l 
        if i <0 :
            i = i + len(person)  
        person[i] += 1  
    cnt += 1

print (cnt)