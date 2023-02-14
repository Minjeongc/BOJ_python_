color = ['black', 'brown' , 'red', 'orange', 'yellow', 'green', 
'blue', 'violet', 'grey', 'white']

one = input()
two = input()
three = input()
result = 0

for i in color:
    if one == i:
        result += (color.index(i) * 10)

    if two == i:
        result += color.index(i)


for j in color:
    if three == j:
        result = result * (10**(color.index(j)))


print(result)