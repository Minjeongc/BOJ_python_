

hour, min, sec = map(int, input().split())

time= int(input())

sec += time
if sec >= 60:
    min += sec // 60
    sec = sec % 60

if min >= 60: 
    hour += min // 60
    min = min % 60

if hour >= 24:
    hour = hour % 24



print(hour, min, sec) 

