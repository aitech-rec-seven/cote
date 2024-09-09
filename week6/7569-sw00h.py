from collections import deque

# 입력 받기
m, n, h = map(int, input().split())

# 3차원 배열 생성
array = []
queue = deque()

for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):
            if row[k] == 1:
                queue.append((i, j, k))  # 익은 토마토 위치 추가
        layer.append(row)
    array.append(layer)

# 방향 설정 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def tomato():
    while queue:
        z, x, y = queue.popleft()

        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy

            # 범위를 벗어나지 않고 안 익은 토마토인 경우
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and array[nz][nx][ny] == 0:
                array[nz][nx][ny] = array[z][x][y] + 1  # 하루가 지날 때마다 1씩 더해줌
                queue.append((nz, nx, ny))


tomato()

max_day = 0
for layer in array:
    for row in layer:
        for tomato in row:
            if tomato == 0:  # 익지 않은 토마토가 있다면 -1 출력
                print(-1)
                exit(0)
        max_day = max(max_day, max(row))

print(max_day - 1)
