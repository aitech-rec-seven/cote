#10799
import sys
input=sys.stdin.readline
lesier=input().rstrip()
lesier=lesier.replace('()','*')
stack=[]
result=0
for i in lesier:    
    if i=='(':
        stack.append(i)
    elif i=='*':
        result+=len(stack)
    elif stack and i==")":
        stack.pop() 
        result+=1
print(result)