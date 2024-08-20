import sys

stack = []
input_data = sys.stdin.read().strip()
commands = input_data.splitlines()

for c in commands:
    if c.startswith('push'):
        stack.append(int(c.split()[1]))
    elif c == 'pop':
        print(stack.pop(0) if stack else -1)
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        print(int(not stack))
    elif c == 'front':
        print(stack[0] if stack else -1)
    elif c == 'back':
        print(stack[-1] if stack else -1)