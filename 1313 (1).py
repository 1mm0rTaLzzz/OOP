size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(map(int, input().split())))

for n in range(size + 1):
    for i in reversed(range(n)):
        print(matrix[i][n - i - 1], end=" ")

for step in range(1, size):
    for i in reversed(range(step, size)):
        print(matrix[i][size - i + (step - 1)],  end=" ")