
n, m = map(int,input().split())
#v = [False for _ in range(n)]
v = [False]* n
#arr = [0 for _ in range(m)]
arr = [0]*m


def dfs(n,m,depth):
    if m == depth:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(0, n):
        if not v[i]:
            v[i] = True
            arr[depth] = i+1
            dfs(n,m,depth+1) 
            #if depth == i:
            v[i] = False
dfs(n,m,0)