import sys
from collections import deque
input = sys.stdin.readline

N= int(input())
array=deque(list(map(int,input().split())))
op=list(map(int,input().split()))
max_n=-1000000000
min_n=1000000000
sum=array.popleft()

def backtracking(N,array,op,sum):
    global max_n,min_n
    if N==1:
        if sum<min_n:
            min_n=sum
        if sum>max_n:
            max_n=sum
        return
    # print(N,sum,op,array)
    tmp=array.popleft()
    for i in range(4):
        if i==0 and op[i]!=0:
            op[i]-=1
            backtracking(N-1,array,op,sum+tmp)
            op[i]+=1
        elif i==1 and op[i]!=0:
            op[i]-=1
            backtracking(N-1,array,op,sum-tmp)
            op[i]+=1
        elif i==2 and op[i]!=0:
            op[i]-=1
            backtracking(N-1,array,op,sum*tmp)
            op[i]+=1
        elif i==3 and op[i]!=0:
            if sum<0:
                op[i]-=1
                backtracking(N-1,array,op,-((-sum)//tmp))
                op[i]+=1
            else:
                op[i]-=1
                backtracking(N-1,array,op,sum//tmp)
                op[i]+=1
    array.appendleft(tmp)

backtracking(N,array,op,sum)
print(max_n)
print(min_n)