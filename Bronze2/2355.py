a, b = map(int, input().split())
result = 0 

if a<=b:
    result = (b*(b+1)//2) - (a*(a+1)//2) + a
else:
    result = (a*(a+1)//2) - (b*(b+1)//2) + b

print(result)