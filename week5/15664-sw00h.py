# 15664
from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

result = set(combinations(numbers, M))

for i in sorted(result):
    print(*i)