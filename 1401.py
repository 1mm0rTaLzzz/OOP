def FillBoard(n, point_x, point_y, x, y):
    global c
    if n == 2:
        for i in range(2):
            for j in range(2):
                if (x + i != point_x) or (y + j != point_y):
                    Board[x + i][y + j] = int(c / 3)
                    c += 1
        return
    else:
        for i in range(2):
            for j in range(2):
                if (x + i * n / 2 > point_x) or (point_x >= x + i * n / 2 + n / 2) or (y + j * n / 2 > point_y) or (point_y >= y + j * n / 2 + n / 2):
                    Board[x + int(n / 2) - 1 + i][y + int(n / 2) - 1 + j] = c / 3
                    c += 1

        for i in range(2):
            for j in range(2):
                if (x + i * n / 2 <= point_x) and (point_x < x + i * n / 2 + n / 2) and (y + j * n / 2 <= point_y) and (point_y < y + j * n / 2 + n / 2):
                    FillBoard(int(n / 2), point_x, point_y, x + i * int(n / 2), y + j * int(n / 2))
                else:
                    FillBoard(int(n / 2), x + int(n / 2) - 1 + i, y + int(n / 2) - 1 + j, x + i * int(n / 2), y + j * int(n / 2))


n = int(input())
n = 2 ** n
c = 3
Board = [[0] * n for i in range(n)]
point_x, point_y = map(int, input().split())
FillBoard(n, 0, 0, point_x - 1, point_y - 1)
for i in range(n):
    for j in range(n):
        print(int(Board[i][j]), end=' ')
    print()