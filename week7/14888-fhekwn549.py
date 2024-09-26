n = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_value, min_value = -10**9, 10**9

def dfs(idx, result, plus, minus, mul, div): # 계산할 뒤의 값 인덱스, 이전계산결과, 연산자 남은수
  global max_value, min_value
  if -10**9 > result or result > 10**9:
      return

  if idx == n:
      max_value = max(max_value, result)
      min_value = min(min_value, result)
      return

  if plus > 0:
      dfs(idx + 1, result + arr[idx], plus-1, minus, mul, div)
  if minus > 0:
      dfs(idx + 1, result - arr[idx], plus, minus-1, mul, div)
  if mul > 0:
      dfs(idx + 1, result * arr[idx], plus, minus, mul-1, div)
  if div > 0:
      dfs(idx + 1, int(result/arr[idx]), plus, minus, mul, div-1)

dfs(1, arr[0], plus, minus, mul, div)
print(max_value)
print(min_value)
