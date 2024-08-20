import sys

stack = []
input_data = sys.stdin.read().strip()
commands = input_data.splitlines()
# commands = ['14', 'push 1', 'push 2', 'top', 'pop', 'size', 'empty', 'pop', 'pop', 'empty']

for c in commands:
    if c.startswith('push'):
        stack.append(int(c.split()[1]))
    elif c == 'pop':
        print(stack.pop() if stack else -1)
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        print(int(not stack))
    elif c == 'top':
        print(stack[-1] if stack else -1)