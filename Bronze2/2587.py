import sys
arr = []
avg = 0
for _ in range(5):
    x = int(sys.stdin.readline().rstrip('\n'))
    arr.append(x)
    avg += x
    
arr.sort()

print(avg//5)
print(arr[2])

