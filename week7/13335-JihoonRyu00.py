import sys

input = sys.stdin.readline

def main():
    n, w, L = map(int, input().rstrip().split())
    w_list = list(map(int, input().rstrip().split()))
    
    i=0
    t=0
    weights=0
    queue=[]

    while True:
        t+=1
        
        for x in queue:
            x[0] -= 1

        if queue and queue[0][0]==0:
            weights-=queue[0][1]
            queue.pop(0)
            
        if i>=n and not queue:
            break

        if len(queue)<w and i<n and weights+w_list[i]<=L:
            # trucks+=1
            weights+=w_list[i]
            queue.append([w,w_list[i]])
            i+=1
    
    print(t)

main()

# input 크기: 
# 시간복잡도: 
# 공간복잡도: 
