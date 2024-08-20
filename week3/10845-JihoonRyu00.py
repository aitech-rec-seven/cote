import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    queue = []
    results = []

    for i in range(1, N+1):
        com = data[i].split()

        if com[0] == "push":
            queue.append(int(com[1]))

        elif com[0] == "pop":
            if queue:
                results.append(str(queue.pop(0)))
            else:
                results.append("-1")

        elif com[0] == "size":
            results.append(str(len(queue)))

        elif com[0] == "empty":
            if queue:
                results.append("0")
            else:
                results.append("1")

        elif com[0] == "front":
            if queue:
                results.append(str(queue[0]))
            else:
                results.append("-1")

        elif com[0] == "back":
            if queue:
                results.append(str(queue[-1]))
            else:
                results.append("-1")
        
        else:
            pass

    print("\n".join(results))

main()

# 시간: 44ms
# input 크기: N(=len(data))
# 시간복잡도: O(N^2) (worst case) -> deque 쓰면 O(N) 가능
# 공간복잡도: O(N)