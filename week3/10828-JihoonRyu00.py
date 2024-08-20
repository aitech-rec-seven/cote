# def main():
#   N = int(input())
#   stack = []

#   for i in range(N):
#     com = input().split()

#     if com[0] == "push":
#       stack.append(int(com[1]))

#     elif com[0] == "pop":
#       if stack:
#         print(stack.pop())
#       else:
#         print(-1)

#     elif com[0] == "size":
#       print(len(stack))

#     elif com[0] == "empty":
#       if stack:
#         print(0)
#       else:
#         print(1)

#     elif com[0] == "top":
#       if stack:
#         print(stack[-1])
#       else:
#         print(-1)

#     else:
#       pass

# main()

# 시간: 500ms

# python list에는 isEmpty()가 따로 없어서 len(list) == 0 사용해야 함
# 하지만 if문을 사용한 코드가 "pythonic"한 코드
# if list: -> list가 not empty면 True, empty면 False 리턴

import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    stack = []
    results = []

    for i in range(1, N + 1):
        com = data[i].split()

        if com[0] == "push":
            stack.append(int(com[1]))

        elif com[0] == "pop":
            if stack:
                results.append(str(stack.pop()))
            else:
                results.append("-1")

        elif com[0] == "size":
            results.append(str(len(stack)))

        elif com[0] == "empty":
            if stack:
                results.append("0")
            else:
                results.append("1")

        elif com[0] == "top":
            if stack:
                results.append(str(stack[-1]))
            else:
                results.append("-1")

        else:
            pass
        
    print("\n".join(results))

main()

# sys.stdin.read를 사용하여 모든 입력을 한번에 읽어서 메모리에 저장한 후, 필요한 대로 이를 처리

# 시간: 44ms
# input 크기: N(=len(data))
# 시간복잡도: O(N)
# 공간복잡도: O(N)