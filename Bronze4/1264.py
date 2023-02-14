
while True:
    s = input()
    s = s.upper()
    count = 0

    for i in s:
        if i == 'A':
            count += 1
        elif i == 'E': 
            count += 1
        elif i == 'I': 
            count += 1
        elif i == 'O': 
            count += 1
        elif i == 'U': 
            count += 1

    

    if s == "#":
        break
    print(count)

    