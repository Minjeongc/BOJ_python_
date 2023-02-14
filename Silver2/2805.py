n, m = map(int, input().split())

tree = list(map(int, input().split()))


start = 1 #min(tree) 가 아님. 
end = max(tree)

while start <= end:
    mid = (start + end )//2
    sp_tree = 0
    for i in tree:
        if i > mid :
            sp_tree += (i-mid)
    if sp_tree  >= m:
        start = mid + 1
        #sp>= m : 의 차이. 
    else:
        end = mid - 1

print(end)