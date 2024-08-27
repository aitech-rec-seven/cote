'''
백준 4949번: 균형잡힌 세상
https://www.acmicpc.net/problem/4949

1. '.' 은 탈출(=끝)
2. '(' 와 '[' 는 스택에 넣음
3. ')' 일때,
- 스택이 비어있으면 -> 꺼내올께(='(')가 없으므로 -> 'no'
- 스택에 '('가 있으면 -> pass
- 스택에 '('가 없으면 -> 'no'
4. ']' 일때,
- 스택이 비어있으면 -> 꺼내올께(='[')가 없으므로 -> 'no'
- 스택에 '['가 있으면 -> pass
- 스택에 '['가 없으면 -> 'no'
5. 문자 전체를 봤는데 스택에 값이 남았을때 -> 'no'


'''
import sys

res_lst = []
while True:
    data = input()

    if data == '.':    #1
        # print('yes')
        res_lst.append('yes')
        break
    
    box = []
    flag = True
    for x in data:
        if (x == '(') or (x == '['):    #2
            box.append(x)

        elif x == ')':    #3
            if not len(box):
                # print('no')
                res_lst.append('no')

                flag = False
                break
            else:
                y = box.pop(-1)
                if y == '(':
                    pass
                else:
                    # print('no')
                    res_lst.append('no')
                    flag = False
                    break
        
        elif x == ']':    #4
            if not len(box):
                # print('no')
                res_lst.append('no')
                flag = False
                break
            else:
                y = box.pop(-1)
                if y == '[':
                    pass
                else:
                    # print('no')
                    res_lst.append('no')
                    flag = False
                    break
    if flag:
        if len(box):
            # print('no')
            res_lst.append('no')
        else:
            # print('yes')
            res_lst.append('yes')

print('\n'.join(res_lst[:-1]))
