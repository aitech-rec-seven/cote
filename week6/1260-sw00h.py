from collections import deque

# DFS 함수
def dfs(graph, v, visited):
    visited[v] = True   # 방문 표시
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 리스트 정렬
for i in range(1, n + 1):
    graph[i].sort()
# print(graph)

# DFS
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# BFS
visited = [False] * (n + 1)
bfs(graph, v, visited)
