''' 
백준 1260번: DFS와 BFS
https://www.acmicpc.net/problem/1260



'''


# 시간 초과 발생함
def func(arr, visited, snode, mode='BFS'):
    if mode == 'BFS':
        n = 0
    else:    # 'DFS'
        n = -1

    box = [snode]    # 스택용
    res = []    # 결과반환용

    while box:
        node = box.pop(n)
        if str(node) not in res:
            res.append(str(node))

        for idx, val in enumerate(arr):
            if (node in val) and (visited[idx] == False):
                
                visited[idx] = True
                box.append(val[0])
                box.append(val[1])
                break

    return ' '.join(res)


# 아래 함수는 통과됨

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
    # N, M, V = 4, 5, 1
    # arr = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

    N, M, V = list(map(int, input().split()))

    # arr = list( list(map(int, input().split())) for _ in range(M))
    # arr.sort()

    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = [False]*(N+1)
    res_dfs = DFS(arr, visited, snode=V)

    visited = [False]*(N+1)
    res_bfs = BFS(arr, visited, snode=V)
   
    print(res_dfs)
    print(res_bfs)
    



if __name__=="__main__":
    main()