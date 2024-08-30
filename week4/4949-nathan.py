import sys
input=sys.stdin.readline
while 1:
    flag=0
    string=input().rstrip()
    if string=='.':
        break
    stack=[]
    for i in string:
        if i=='[' or i=='(':
            stack.append(i)
        elif not stack and (i==']' or i==')'):
            flag=1
            break
        elif stack and i==']' or i==')':
            if  stack[-1]=="[" and i==']':
                stack.pop()
            elif stack[-1]=='(' and i==')':
                stack.pop()
            else:
                flag=1
                break
    if not stack and flag==0:
        print('yes')
    elif stack or flag==1:
        print('no')

