n = int(input())
com_list = []
num_list = []
for _ in range(n):
  np = str(input())
  if " " in np:
    com, x = np.split()
    com_list.append([com,x])
  else : 
    com = np
    com_list.append([com])
for i in com_list:
  if len(i) == 2:
    num_list.append(i[1])
  else:
    if i[0] == 'front':
      if len(num_list) == 0:
        print("-1")
      else:
        print(num_list[0])
    elif i[0] == 'back':
      if len(num_list) == 0:
        print("-1")
      else:
        print(num_list[-1])
    elif i[0] == 'size':
      print(len(num_list))
    elif i[0] == 'empty':
      if len(num_list) == 0:
        print("1")
      else:
        print("0")
    elif i[0] == 'pop':
      if len(num_list) == 0:
        print("-1")
      else:
        print(num_list[0])
        del num_list[0]
