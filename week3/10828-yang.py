# 백준 10828번 스택
# https://www.acmicpc.net/problem/10828

'''
input
- push
- pop
- size
- empty
- top

'''

''' 
방법 1
백준에서 Python3로 실행시 시간 초과 발생함
PyPy3로 실행시 성공함(시간: 384 ms)
'''
N = int(input())
box = []
for _ in range(N):
    command_lst = input().split(' ')

    if len(command_lst) == 2:    # push
        command, num = command_lst
        num = int(num)
        box.append(num)
    else:
        res = 0
        command = command_lst[0]
        if command == 'pop':
            if len(box):    # box len = 1
                res = box.pop(-1)
            else:
                res = -1
        elif command == 'top':
            if len(box):
                res = box[-1]
            else:
                res = -1
        elif command == 'size':
            res = len(box)
        else:    # empty
            if len(box):
                res = 0
            else:
                res = 1
        print(res)




'''
방법 2
위 방법에서 len 함수 사용 X
Python3로 실행 시 성공함(시간: 500 ms)
PyPy3로 실행시 성공함(시간: 388 ms)
'''
N = int(input())
box = []
cnt = 0
for _ in range(N):
    command_lst = input().split(' ')

    if len(command_lst) == 2:    # push
        command, num = command_lst
        num = int(num)
        box.append(num)
        cnt += 1
    else:
        res = 0
        command = command_lst[0]
        if command == 'pop':
            if cnt > 0:    # box len = 1
                res = box.pop(-1)
                cnt -= 1
            else:
                res = -1
        elif command == 'top':
            if cnt > 0:
                res = box[-1]
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
