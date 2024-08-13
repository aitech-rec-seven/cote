# 백준 10808번 알파벳 개수
# https://www.acmicpc.net/problem/10808

'''
input: 알파벳 소문자 단어 

output: 알파벳별 개수

'''

import string


data = input()

lower_lst = [i for i in string.ascii_lowercase]    # 소문자 리스트
# print(lower_lst)

res = []
for lower in lower_lst:
    cnt = data.count(lower)
    res.append(str(cnt))
print(' '.join(res))
