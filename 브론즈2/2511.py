a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum1 = 0
sum2 = 0
score = []

for i in range(10):
    if a[i] > b[i]:
        sum1 += 3
        score.append('A')
    elif a[i] == b[i]:
        sum1 += 1
        sum2 += 1
        score.append('D')
    else:
        sum2 += 3
        score.append('B')
for i in reversed (score):
    if i == 'A' :
        last = 'A'
        break 
        
    elif i == 'B':
        last = 'B'
        break
    else :
        last = ''

print(sum1, sum2)

if score.count('A') > score.count('B'):
    print('A')
elif score.count('B') > score.count('A'):
    print('B')
elif ((score.count('A') == score.count('B') )and (last =='A')):
    print('A')
elif ((score.count('A') == score.count('B') )and (last =='B')):
    print('B')
else:
    print('D')