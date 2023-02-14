word = input()

for i in word:
    temp = ord(i)
    if temp >= 65 and temp <= 77:
        print(chr(temp+13) , end = "")
    elif temp >= 78 and temp <=90:
        print(chr(temp-13) , end = "")
    elif temp >= 97 and temp <= 109:
        print(chr(temp+13), end = "")
    elif temp >= 110 and temp <= 122 : 
        print(chr(temp-13), end = "")
    else:
        print(i, end = "")