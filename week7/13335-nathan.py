import  sys
from collections import deque
input = sys.stdin.readline

n, w,l = map(int,input().split())
lst=list(map(int,input().split()))
lst=deque(lst)
t=0
weight=deque([0]*w)

while lst or sum(weight)>0:
    t+=1
    weight.popleft()

    if lst:
        if lst[0]+sum(weight)<=l:
            weight.append(lst.popleft())
        else:
            weight.append(0)
print(t)
        




