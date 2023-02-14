a,b,c= map(int, input().split())#구하는게 n

if b>=c:
    n=-1
else:
    n = a//(c-b)+1

print(n)