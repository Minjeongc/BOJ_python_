arr = input()

for i in arr:
    i = ord(i)
    if i >=68 and i <=90:
        i -= 3
        i = chr(i)
    else:
        i += 23
        i = chr(i)
    print(i, end = "")

