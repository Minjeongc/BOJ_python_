alpha = input()
result = 0

for i in alpha:
    num = ord(i)   
    result += 2
    if num<65:
        break
    elif num <= 67: ##ABC
        result +=1
    elif num<= 70: ##DEF
        result +=2
    elif num <=73: ##GHI
        result +=3
    elif num <=76: ##JKL
        result +=4
    elif num <= 79: #MNO
        result +=5
    elif num <= 83: #PQRS
        result +=6
    elif num <=86:
        result +=7 ##TUV
    else:
        result +=8

print(result)
