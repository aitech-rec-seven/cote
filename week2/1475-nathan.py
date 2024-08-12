import sys

input=sys.stdin.readline

string=input().strip()
lst=[0]*10
for i in range(10):
    lst[i]+=string.count(str(i))
if lst[6]> lst[9]:
    k=(lst[6]-lst[9])
    lst[9]+=k//2
    lst[6]-=k//2
else:
    k=(lst[9]-lst[6])
    lst[6]+=k//2
    lst[9]-=k//2
print(max(lst))
# for i in range(10):
#     if string[i]=='6' or string[i]=='9':
#         if lst[6]>lst[9]:
#             lst[9]+=1
#         else:
#             lst[6]+=1
#     else:
#         lst[i]+=1
# print(max(lst))