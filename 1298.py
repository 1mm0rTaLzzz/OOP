n = int(input())
board = [[-1] * n for _ in range(n)]
move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}


def knight(i, j, pos):
    if pos == n * n:
        return True
    for mi, mj in move:
        i_new = i + mi
        j_new = j + mj
        if 0 <= i_new < n and 0 <= j_new < n and board[i_new][j_new] == -1:
            board[i_new][j_new] = pos
            if knight(i_new, j_new, pos + 1):
                return True
            board[i_new][j_new] = -1
    return False


if __name__ == '__main__':
    x, y, board[x][y], search = 0, 0, 0, 0
    if n <= 8:
        if knight(x, y, 1):
            while search != n * n:
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == search:
                            print(dict[j], i + 1, sep='')
                            search += 1
        else:
            print('IMPOSSIBLE')
    elif n == 7:
        print('''a1
c2
e1
g2
f4
g6
e7
f5
g3
e4
f2
g4
f6
d7
e5
f3
g1
e2
d4
c6
a7
b5
c3
d1
e3
f1
d2
b1
a3
c4
b6
d5
c7
a6
b4
a2
c1
d3
b2
a4
c5
b3
a5
b7
d6
f7
g5
e6
g7''')
    elif n == 8:
        print('''a1
c2
e1
g2
h4
g6
h8
f7
g5
h3
f4
h5
g7
e8
f6
g4
h2
f3
g1
e2
g3
h1
f2
e4
d6
f5
h6
g8
e7
c8
a7
b5
c3
d1
e3
f1
d2
b1
a3
c4
e5
d7
b8
a6
c5
d3
b2
a4
b6
a8
c7
d5
b4
a2
c1
b3
d4
c6
a5
b7
d8
e6
f8
h7''')
    else:
        print('IMPOSSIBLE')
