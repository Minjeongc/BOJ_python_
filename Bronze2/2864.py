#최대, 최소만 구하면 되므로 모두 5인경우, 모두 6인경우로 확인하기!
n , m= input().split()

n = n.replace('5', '6')
m = m.replace('5', '6')

max_num = int(n) + int (m)

n = n.replace('6', '5')
m = m.replace('6', '5')

min_num = int(n) + int (m)

print(min_num , max_num)

