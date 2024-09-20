''' 
백준 1260번: DFS와 BFS
https://www.acmicpc.net/problem/1260

'''
def BFS(arr, visited, snode):
    box = [snode]    # 스택용
    res = []    # 결과반환용

    while box:
        node = box.pop(0)
        if not visited[node]:
            visited[node] = True
            res.append(node)
            for i in sorted(arr[node]):
                if not visited[i]:
                    box.append(i)

    return ' '.join(map(str, res))

def DFS(arr, visited, snode):
    box = [snode]    # 스택용
    res = []    # 결과반환용

    while box:
        node = box.pop(-1)
        if not visited[node]:
            visited[node] = True
            res.append(node)
            for i in sorted(arr[node], reverse=True):
                if not visited[i]:
                    box.append(i)

    return ' '.join(map(str, res))

def main():
    # ex) N, M, V = 4, 5, 1
    # ex) arr = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

    N, M, V = list(map(int, input().split()))

    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    # ex) arr = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

    visited = [False]*(N+1)
    res_dfs = DFS(arr, visited, snode=V)

    visited = [False]*(N+1)
    res_bfs = BFS(arr, visited, snode=V)
   
    print(res_dfs)
    print(res_bfs)

    # ex) 1 2 4 3
    # ex) 1 2 3 4
    


if __name__=="__main__":
    main()