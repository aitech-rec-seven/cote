from collections import deque
import sys

queue = deque()
output = []

nums = int(sys.stdin.readline().strip())

for _ in range(nums):
    command = sys.stdin.readline().strip().split(' ')

    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if queue:
            output.append(queue.popleft())
        else:
            output.append(-1)

    elif command[0] == 'size':
        output.append(len(queue))

    elif command[0] == 'empty':
        output.append(0 if queue else 1)

    elif command[0] == 'front':
        if queue:
            output.append(queue[0])
        else:
            output.append(-1)

    elif command[0] == 'back':
        if queue:
            output.append(queue[-1])
        else:
            output.append(-1)

sys.stdout.write('\n'.join(map(str, output)) + '\n')