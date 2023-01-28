angle = [int(input())for _ in range(3)]

count = 0
sum = 0
same = 0

for i in angle:
    sum += i 
    if i == 60:
        count += 1

angle.append(angle[0])

for i in range(3):
    if angle[i] == angle[i+1]:
        same += 1

if count == 3:
    print("Equilateral")
elif sum != 180:
    print("Error")
elif sum == 180 and same == 0:
    print("Scalene")
else:
    print("Isosceles")
