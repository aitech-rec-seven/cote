import sys
from collections import deque
input = sys.stdin.readline

M,N,H= map(int,input().split())
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))
step=[(-1,0),(1,0),(0,1),(0,-1),(N,0),(-N,0)]
dis=[[M+N*H+1 for i in range(M)] for j in range(N*H)]
initial=[]
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            initial.append([i,j])
            dis[i][j]==0
        elif board[i][j]==-1:
            dis[i][j]=-1
def bfs(board,initial,dis):

    queue=deque(initial)
    while queue:
        current=queue.popleft()

        for i in step:
            dx,dy=i[0],i[1]
            next_x,next_y=current[0]+dx,current[1]+dy
            if 0<=next_x<N*H and 0<=next_y<M and board[next_x][next_y]==0:
                dis[next_x][next_y]=min(dis[next_x][next_y],dis[current[0]][current[1]]+1)
    return dis
dis = bfs(board,initial,dis)
print(dis)



    