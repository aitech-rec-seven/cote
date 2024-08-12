import sys
input = sys.stdin.readline
ctr = sorted(list(input().strip()))
lst=[0]*26
for i in ctr:
    lst[ord(i)-97]+=1
print(*lst)

