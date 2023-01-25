print(*(lambda x: (x[0][0] - x[2][0], x[0][1] - x[1][1]))
([list(map(lambda x: int(x), input().split())) for i in range(3)]))