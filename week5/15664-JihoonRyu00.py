import sys

input = sys.stdin.readline


def dodo(arr, N, M, result):
    if M == 0:
        print(*result)
    for i in range(N):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        result_temp = result + [arr[i]]
        arr_temp = arr[i + 1 :]
        N = len(arr_temp)
        dodo(arr_temp, N, M - 1, result_temp)


def main():
    N, M = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    result = []
    dodo(arr, N, M, result)


main()


# input 크기: N
# 시간복잡도: O(N log N + N^M) (정렬: O(N log N) + 조합생성: O(N^M))
# 공간복잡도: O(N * M)
