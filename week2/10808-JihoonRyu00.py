def main():
  S=input()
  list=[0 for i in range(ord('z')-ord('a')+1)]
  for i in S:
    list[ord(i)-ord('a')]+=1
  for i in list:
    print(i, end = " ")

main()

# input 크기: N(=len(S))
# 시간복잡도: O(N)
# 공간복잡도: O(1)
