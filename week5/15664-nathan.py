import sys
input=sys.stdin.readline
N,M= map(int,input().split())
lst=sorted(list(map(int,input().split())))
contain=[]
visited=set()
start=0
def backtracking(lst,contain,M,visited,start):
    
    if len(contain)==M :
        contain_tuple=tuple(contain)
        if contain_tuple not in visited:
            print(*contain)
            visited.add(contain_tuple)
        return
    
    for i in range(start,len(lst)):
        contain.append(lst[i])
        backtracking(lst,contain,M,visited,i+1)
        t=contain.pop()

backtracking(lst,contain,M,visited,0)

