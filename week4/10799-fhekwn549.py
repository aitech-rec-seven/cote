task = input()
stack=[]
cnt = 0
for i in range(len(task)):
    if task[i] == "(":
        stack.append("(")
    else : ## task[i] == ")"
        if task[i-1]=="(":
            stack.pop()
            cnt+=len(stack)

        else :
            stack.pop()
            cnt+=1 
print(cnt)
