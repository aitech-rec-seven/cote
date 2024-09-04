import sys
input=sys.stdin.readline

N=int(input())
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))
global blue,white
blue=0
white=0
def dfs(board,N):
    global blue, white

    unique=True
    first_value=board[0][0]
    for row in board:
        for cell in row:
            if cell!=first_value:
                unique=False
                break
        if not unique:
            break

    if unique:
        if 1 in list(set(board[0])):
            blue+=1
        else:
            white+=1
        return 
    else:
        cut_board1=[row[:N//2] for row in board[:N//2]]
        cut_board2=[row[:N//2] for row in board[N//2:]]
        cut_board3=[row[N//2:] for row in board[:N//2]]
        cut_board4=[row[N//2:] for row in board[N//2:]]
        dfs(cut_board1,N//2)
        dfs(cut_board2,N//2)
        dfs(cut_board3,N//2)
        dfs(cut_board4,N//2)
dfs(board,N)
print(white)
print(blue)