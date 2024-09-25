n, w, L = map(int, input().split())
T = list(map(int, input().split()))

B = [0] * w
st = 0
while len(B) > 0: 
  st += 1
  B.pop(0) 
  if T:
    if sum(B) + T[0] <= L:
      B.append(T.pop(0))
    else:
      B.append(0)  
print(st)
