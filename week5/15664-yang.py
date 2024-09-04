'''
백준 15664번: N과 M(10)
 https://www.acmicpc.net/problem/15664


input
4 2
9 7 9 1

output
1 7
1 9
7 9
9 9

'''

from itertools import combinations


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()    # 정렬

combination_lst = combinations(numbers, M)    # 조합 (중복 X)
combination_lst = list(set(list(combination_lst)))
combination_lst.sort()

for comb in combination_lst:
    for val in comb:
        print(val, end=' ')
    print()
