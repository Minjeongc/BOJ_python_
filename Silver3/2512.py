num = int(input())

budget = list(map(int, input().split()))
sum_budget = int(input())

start = 1
end = max(budget)

while start <= end :

    mid = (start + end) // 2
    temp = 0

    for i in budget:
        if mid < i :
            temp += mid
        else:
            temp += i
    if temp <= sum_budget :
        start = mid + 1
    else :
        end = mid - 1

print(end)
