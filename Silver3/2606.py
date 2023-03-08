computer = int(input())
line = int(input())

graph =[[]for _ in range(computer+1)]

visited = [0] * (computer+1)

for _ in range(line):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for n in graph[v]:
        if visited[n] == 0:
            dfs(n)

dfs(1)
print(sum(visited)-1)