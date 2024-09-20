from collections import deque

# DFS 함수 정의 (재귀 방식)
def dfs(v, visited, graph):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 방문한 노드 출력

    # 인접 노드를 작은 숫자부터 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)

# BFS 함수 정의 (큐를 사용)
def bfs(start, visited, graph):
    queue = deque([start])  # 시작 노드를 큐에 넣음
    visited[start] = True  # 현재 노드를 방문 처리

    while queue:
        v = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        print(v, end=' ')  # 방문한 노드 출력

        # 인접 노드를 작은 숫자부터 방문
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)  # 큐에 인접 노드를 추가
                visited[i] = True  # 방문 처리

# 입력 받기
n, m, v = map(int, input().split())  # 정점의 개수, 간선의 개수, 시작 정점

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트를 오름차순으로 정렬
for i in range(1, n+1):
    graph[i].sort()

# 방문 리스트 초기화 (DFS와 BFS 각각 사용)
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# DFS 실행
dfs(v, visited_dfs, graph)
print()  # 줄바꿈

# BFS 실행
bfs(v, visited_bfs, graph)
print()  # 줄바꿈
