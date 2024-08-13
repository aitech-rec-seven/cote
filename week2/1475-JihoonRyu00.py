# def main():
#   n=int(input())
#   max_=0
#   for i in range(10):
#     if i is not 6:
#       max_=max(max_,n.count(str(i)))
#     else:
#       max_=max(max_,n.count("6")+n.count("6"))
#   return max
# 런타임에러

def main():
  n=input()
  m=[0 for i in range(10)]
  for i in n:
    m[int(i)]+=1
  m[6]=int((m[6]+m[9]+1)/2)
  print(max(m[:9]))

main()

# input 크기: N(=len(n))
# 시간복잡도: O(N)
# 공간복잡도: O(1)
