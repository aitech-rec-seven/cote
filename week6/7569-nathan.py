import sys
from collections import deque
input = sys.stdin.readline

M,N,H= map(int,input().split())
board=[]
for i in range(N*H):
    board.append(list(map(int,input().split())))
step=[(-1,0),(1,0),(0,1),(0,-1),(N,0),(-N,0)]
dis=[[M+N*H+1 for j in range(M)] for i in range(N*H)]
initial=[]
for i in range(N*H):
    for j in range(M):
        if board[i][j]==1:
            initial.append([i,j])
            dis[i][j]=0
        elif board[i][j]==-1:
            dis[i][j]=-1

def bfs(board,initial,dis):

    queue=deque(initial)
    while queue:
        current=queue.popleft()

        for i in step:
            dx,dy=i[0],i[1]
            next_x,next_y=current[0]+dx,current[1]+dy
            if (dx==-1 and dy==0) or (dx==1 and dy==0):
                if (next_x)//N!= (current[0])//N:
                    continue
            if 0<=next_x<N*H and 0<=next_y<M and dis[next_x][next_y]==M+N*H+1:
                dis[next_x][next_y]=dis[current[0]][current[1]]+1
                queue.append([next_x,next_y])
               
    return dis
dis = bfs(board,initial,dis)

max_distance=0
for row in dis:
    for cell in row:
        if cell==M+N*H+1:
            print(-1)
            sys.exit()
        if cell>max_distance:
            max_distance=cell
print(max_distance)



    