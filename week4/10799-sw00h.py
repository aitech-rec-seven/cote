data = input()
stack = []
count = 0

for i, char in enumerate(data):
    if char == "(":
        stack.append(char)

    elif char == ")":
        if data[i-1] == "(":
            stack.pop()
            count += len(stack)  # 현재 스택에 남아있는 막대기 수
        else:
            stack.pop()
            count += 1  # 막대

print(count)

# a = "()(((()())(())()))(())"