import sys

input = sys.stdin.readline

white = 0
blue = 0


def cut(N, arr):
    global white, blue
    total = sum([sum(row) for row in arr])

    if total == 0:
        white += 1
    elif total == N**2:
        blue += 1
    else:
        N = N // 2  # N/2는 float return -> index에 사용 불가
        # N==1인 경우는 위 조건에서 다 걸러짐
        cut(N, [row[:N] for row in arr[:N]])
        cut(N, [row[:N] for row in arr[N:]])
        cut(N, [row[N:] for row in arr[:N]])
        cut(N, [row[N:] for row in arr[N:]])


def main():
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    cut(N, arr)
    print(white, blue)


main()

# input 크기: N
# 시간복잡도: O(N^2 * log(N))
# 공간복잡도: O(N^2)
