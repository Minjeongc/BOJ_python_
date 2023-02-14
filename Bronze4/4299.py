from sre_constants import MIN_UNTIL


add, minus = input().split()

add = int(add)
minus= int(minus)

x = ( add + minus ) / 2
y = ( add - minus ) / 2


if (x >= 0 and y >= 0):
    if ( x % 1 == 0) and (y % 1 == 0):
        x = int(x)
        y = int(y)
        
        print(max(x,y), min(x,y))
    else:
        print("-1")
else:
    print("-1") 

