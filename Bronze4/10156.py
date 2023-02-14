cost , num , money = input().split()

cost = int(cost)
num = int(num)
money = int(money)

parent = cost*num

if parent > money:
    print(parent-money)
else:
    print("0")