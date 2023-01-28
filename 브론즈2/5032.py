e,f,c = map(int, input().split())

temp = e // c + e %c + f

result = e // c 

while temp >= c :
    result += temp //c 
    temp = (temp % c) + (temp // c)


print(result)