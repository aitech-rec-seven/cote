from collections import deque

# 입력 받기
m, n, h = map(int, input().split())

# 3차원 리스트로 창고 상태 입력받기
matrix = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    matrix.append(layer)

# 6방향 이동을 위한 좌표 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 큐 생성 및 초기 익은 토마토 위치 저장
queue = deque()

# 익은 토마토 위치를 큐에 모두 넣음
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 1:
                queue.append((z, x, y))

# BFS 함수 정의
def bfs():
    while queue:
        z, x, y = queue.popleft()

        # 6방향 탐색
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않는지 체크
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                # 익지 않은 토마토인 경우
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1  # 익게 하고 일수 증가
                    queue.append((nz, nx, ny))

# BFS 수행
bfs()

# 결과 계산
result = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 0:  # 아직 익지 않은 토마토가 있으면
                print(-1)  # -1 출력 후 종료
                exit(0)
            result = max(result, matrix[z][x][y])  # 최대 날짜 계산

# 첫날이 1이었으므로, 최종 일수에서 1을 빼줌
print(result - 1)
