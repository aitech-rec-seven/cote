import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
graph=[[]for i in range(N+1)]
visited=[False]*(N+1)
for i in range(M):
    u,v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
graph=[sorted(lst) for lst in graph]
def dfs(grpah,visited,V):
    
    print(V, end=' ')
    visited[V]=True
    for next in graph[V]:
        if not visited[next]:
            dfs(graph,visited,next)

def bfs(graph,visited,V):

    visited[V]=True
    queue= deque([V])
    while queue:
        current=queue.popleft()
        print(current,end=' ')
        for next in graph[current]:
            if not visited[next]:
                visited[next]= True
                queue.append(next)

    return        

dfs(graph,visited,V)
print()
visited=[False]*(N+1)
bfs(graph,visited,V)
