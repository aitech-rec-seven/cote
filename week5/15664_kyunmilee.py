from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

result = set()
for k in permutations(numbers, m):
    check = 1
    
    for i in range(m-1):
        if k[i] > k[i+1]:
            check = 0
            break
    if check == 1:
        result.add(k)

for seq in sorted(result):
    print(" ".join(map(str, seq)))