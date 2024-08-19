from collections import deque
import sys
input=sys.stdin.readline
lst=deque()
for i in range(int(input())):
    cmd=list(input().split())
    if len(cmd)==2:
        lst.append(int(cmd[-1]))
    else:
        if cmd[0]=='front':
            if lst:
                print(lst[0])
            else:
                print(-1)
        elif cmd[0]=='empty':
            if lst:
                print(0)
            else:
                print(1)

        elif cmd[0]=='pop':
            if lst:
                print(lst.popleft())
            else:
                print(-1)
        elif cmd[0]=='size':
            print(len(lst))

        elif cmd[0]=='back':
            if lst:
                print(lst[-1])
            else:
                print(-1)