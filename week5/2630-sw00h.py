# 2630

def check_and_divide(grid, x, y, size):
    global blue_count, white_count

    initial_color = grid[x][y]  # color 기준
    same_color = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if grid[i][j] != initial_color:
                same_color = False
                break
        if not same_color:
            break

    if same_color:
        if initial_color == 1:
            blue_count += 1
        else:
            white_count += 1
        return
    # 색이 다르면 재귀
    half = size // 2
    top_left = check_and_divide(grid, x, y, half)
    top_right = check_and_divide(grid, x, y + half, half)
    bottom_left = check_and_divide(grid, x + half, y, half)
    bottom_right = check_and_divide(grid, x + half, y + half, half)

N = int(input())  # 크기
grid = [list(map(int, input().split())) for _ in range(N)]

blue_count = 0
white_count = 0

check_and_divide(grid, 0, 0, N)

print(white_count)
print(blue_count)


