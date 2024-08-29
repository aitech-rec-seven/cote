while True:
  txt = input()
  stack = []
  answer = 'yes'
  if txt == '.':
    break
  for i in txt:
    if i=='(' or i=='[': ## 좌괄호 stack 입력
      stack.append(i)
    elif i == ')':  
      if len(stack) == 0: ## 우괄호일 때 stack에 아무것도 없으면 no
        answer = 'no'
        break
      else:
        if stack.pop() != '(':  ## 우괄호일 때 stack에서 pop한게 맞는 좌괄호가 아니면 no
          answer = 'no'
          break
    elif i == ']':
      if len(stack) == 0: 
        answer = 'no'
        break
      else:
        if stack.pop() != '[':
          answer = 'no'
          break
    else:
      continue
  if len(stack) != 0: 
    answer = 'no'
  print(answer)
