hour, min = map(int, input().split())

def calTime(hour, min):
    if min >= 45:
        print(hour, min-45)
    else :
        print(hour-1, 15 + min)
        


if hour != 0 :
   calTime(hour,min)

else:
    if min >= 45:
        print(hour, min-45)
    else:
        print(23 , 15 + min)
    


