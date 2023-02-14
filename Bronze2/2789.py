cam = "CAMBRIDGE"
arr = input()

for i in arr:
    if cam.count(i) != 0:
        arr = arr.replace(i, '')

print(arr)