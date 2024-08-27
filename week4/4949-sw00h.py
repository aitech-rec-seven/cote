lines = []
matching_bracket = {")": "(", "]": "["}

while True:    # 입력
    line = input()
    if line == ".":
        break
    lines.append(line)

for line in lines:  # 줄 처리
    stack = []
    balanced = True

    for char in line:   # 문자 처리
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != matching_bracket[char]:
                balanced = False
                break
            stack.pop()

    if balanced and not stack:  # 균형 검사
        print("yes")
    else:
        print("no")