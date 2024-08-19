import sys
input=sys.stdin.readline
N= int(input())
lst=[]

for i in range(N):
    cmd=input()
    if ' ' in cmd:
        _,num=cmd.split()
        lst.append(int(num))
    else:
        if cmd=='top':
            if lst:
                print(lst[-1])
            else:
                print(-1)
        elif cmd=='size':
            print(len(lst))
        elif cmd=='pop':
            if lst:
                print(lst.pop())
            else:
                print(-1)
        elif cmd=='empty':
            if lst:
                print(0)
            else:
                print(1)
