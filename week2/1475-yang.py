# 백준 1475번 방번호
# https://www.acmicpc.net/problem/1475

'''
- 번호 세트: 0 ~ 9
- 6 -> 9 또는 9 -> 6 이용 가능

output: 세트 개수의 최소값
'''

data = input()
data = data.replace('9', '6')
data = list(map(int, data))

res = 0
while True:
    if len(data) == 0:    # 탈출조건
        break 

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 6]:    # 6이 2개: 0 ~ 8 + 6
        if i in data:
            data.remove(i)
    res += 1

print(res)
