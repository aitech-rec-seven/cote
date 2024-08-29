user_input = input("")
cnt = 0
memory = []
for i in range(len(user_input)):
    if user_input[i] == '(':
        memory.append('(')
    else:
        if len(memory) != 0:
            del memory[-1]
        if user_input[i-1] == '(':
            cnt += len(memory)
        else:
            cnt += 1
print(cnt)