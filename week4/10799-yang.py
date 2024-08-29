'''
백준 10799번: 쇠막대기
https://www.acmicpc.net/problem/10799

크게 4개의 케이스가 존재함
1. )(
2. ()
3. ((
4. ))

ex)
input: ()(((()())(())()))(())
output: 17

'''


data = input()
box = []
res = 0
flag = True
for idx in range(len(data)-1):
    val = data[idx:idx+2]
    if data[idx:idx+2] == ')(':
        if len(box):
            if flag:
                res += 1
            else:
                flag = True
    elif data[idx:idx+2] == '()':
        res += len(box)
        flag = False
    elif data[idx:idx+2] == '((':
        box.append(1)
    elif data[idx:idx+2] == '))':
        if len(box):
            box.pop(-1)
        res += 1

print(res)
