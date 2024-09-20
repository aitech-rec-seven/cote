import sys

input = sys.stdin.readline

def DFS(edges,visited,V,N):
    visited[V]=True
    print(str(V)+" ")
    for i in range(N+1):
        if edges[V][i] and not visited[i]:
          DFS(edges,visited,i,N)

def BFS():
    pass

def main():
    N, M, V = map(int, input().rstrip().split())
    edges = [[False for col in range(N+1)] for row in range(N+1)]
    visited = [False for col in range(N+1)]
    for i in range(M):
        edge = list(map(int, input().rstrip().split()))
        edges[edge[0]][edge[1]]=1
        edges[edge[1]][edge[0]]=1
    print(DFS(edges,visited,V,N))
    


main()

# input 크기: 
# 시간복잡도: 
# 공간복잡도: 
