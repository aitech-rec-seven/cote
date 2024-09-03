def color_same(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                return False, color
    return True, color


def count_paper(x, y, n, white, blue):
    temp, color = color_same(x, y, n)
    
    if temp == True:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        n = n // 2
        white, blue = count_paper(x, y, n, white, blue)
        white, blue = count_paper(x, y+n, n, white, blue)
        white, blue = count_paper(x+n, y, n, white, blue)
        white, blue = count_paper(x+n, y+n, n, white, blue)
    return white, blue

num = int(input())

paper = []
for _ in range(num):
    nums = input().split()
    nums = list(map(int, nums))
    paper.append(nums)
    
white, blue = count_paper(0, 0, num, 0, 0)
print(white)
print(blue)