num = [int(input()) for _ in range(5)] #엔터쳐서 값 입력받기
sum = 0

for i in num : 
    if i < 40:
       sum += 40

    else:
        sum += i
print(int(sum/5)) 