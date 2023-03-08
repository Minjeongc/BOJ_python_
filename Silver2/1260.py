# from collections import deque 

# def dfs(graph, start_node) : 
#     visited = []
#     not_visited = deque()
#     not_visited.append(start_node)
#     while not_visited:
#         node = not_visited.pop()
#         if node not in visited:
#             visited.append(node)
#             temp = list(set(graph[node]) - set(visited))
#             temp.sort(reverse= True)
#             not_visited.extend(temp)
#     return visited

# def bfs(graph, start_node):
#     visited = []
#     not_visited = deque()
#     not_visited.append(start_node)
#     while not_visited:
#         node = not_visited[0]
#         del not_visited[0]
#         if node not in visited:
#             visited.append(node)
#             temp = list(set(graph[node] )- set(visited))
#             temp.sort()
#             not_visited.extend(temp)
#     return visited


# edge, link , start = map(int, input().split())

# graph = {}

# for _ in range(link):
#     n1, n2= map(int, input().split())
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)

# print(*dfs(graph, start))
# print(*bfs(graph, start))

from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, s, visited):
    que = deque([s])
    visited[s] = True
    while que:
        v = que.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    temp_li = list(map(int, input().split()))
    graph[temp_li[0]].append(temp_li[1])
    graph[temp_li[1]].append(temp_li[0])

for i in range(n+1):
    graph[i].sort()

visited = [False]*(n+1) 
dfs(graph,v,visited) 
print() 
visited = [False]*(n+1)
bfs(graph,v,visited) 