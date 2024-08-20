# 백준 10845번 큐
# https://www.acmicpc.net/problem/10845

'''
input
- push
- pop
- size
- empty
- front
- back

'''

'''
방법 1
Python3로 실행시 시간 초과 발생함
PyPy3로 실행시 성공함(시간: 392 ms)
'''
N = int(input())

box = []
cnt = 0
for _ in range(N):
    command_lst = input().split(' ')

    if len(command_lst) == 2:    # push
        command, num = command_lst
        command = command.strip()
        num = num.strip()
        num = int(num)
        box.append(num)
        cnt += 1
    else:
        res = 0
        command = command_lst[0]
        command = command.strip()
        if command == 'pop':
            if cnt > 0:    # box len = 1
                res = box.pop(0)
                cnt -= 1
            else:
                res = -1
        elif command == 'back':
            if cnt > 0:
                res = box[-1]
            else:
                res = -1
        elif command == 'front':
            if cnt > 0:
                res = box[0]
            else:
                res = -1
        elif command == 'size':
            res = cnt
        else:    # empty
            if cnt > 0:
                res = 0
            else:
                res = 1
        print(res)



'''
방법 2: 위 방법과 input 입력 방법이 다름
Python3로 실행시 (시간: 44 ms)
'''
import sys
N = int(sys.stdin.readline())

box = []
cnt = 0
for _ in range(N):
    command_lst = sys.stdin.readline().split(' ')

    if len(command_lst) == 2:    # push
        command, num = command_lst
        command = command.strip()
        num = num.strip()
        num = int(num)
        box.append(num)
        cnt += 1
    else:
        res = 0
        command = command_lst[0]
        command = command.strip()
        if command == 'pop':
            if cnt > 0:    # box len = 1
                res = box.pop(0)
                cnt -= 1
            else:
                res = -1
        elif command == 'back':
            if cnt > 0:
                res = box[-1]
            else:
                res = -1
        elif command == 'front':
            if cnt > 0:
                res = box[0]
            else:
                res = -1
        elif command == 'size':
            res = cnt
        else:    # empty
            if cnt > 0:
                res = 0
            else:
                res = 1
        print(res)
