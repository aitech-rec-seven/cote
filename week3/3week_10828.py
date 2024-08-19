'''nums = int(input(""))
stacks = []
if 1<= nums <= 10000:
    for i in range(nums):
        order = input("").split(' ')
        if order[0] == 'push':
            stacks.append(order[1])
        if order[0] == 'pop':
            if len(stacks) != 0:
                print(stacks[-1])
                del stacks[-1]
            else:
                print(-1)
        if order[0] == 'size':
            print(len(stacks))
        if order[0] == 'empty':
            if len(stacks) == 0:
                print(1)
            else:
                print(0)
        if order[0] == 'top':
            if len(stacks) == 0:
                print(-1)
            else:
                print(stacks[-1])'''

import sys

nums = int(sys.stdin.readline().strip())
stacks = []
output = []

for i in range(nums):
    order = sys.stdin.readline().strip().split(' ')
    
    if order[0] == 'push':
        stacks.append(order[1])
    
    elif order[0] == 'pop':
        if len(stacks) != 0:
            output.append(stacks.pop())
        else:
            output.append(-1)
    
    elif order[0] == 'size':
        output.append(len(stacks))
    
    elif order[0] == 'empty':
        if len(stacks) == 0:
            output.append(1)
        else:
            output.append(0)
    
    elif order[0] == 'top':
        if len(stacks) == 0:
            output.append(-1)
        else:
            output.append(stacks[-1])

sys.stdout.write('\n'.join(map(str, output)) + '\n')