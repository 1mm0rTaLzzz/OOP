from math import pi, sqrt

count, radius = map(float, input().split())

length = 2 * pi * radius
x, y = [], []
for _ in range(int(count)):
    [method(digit) for digit, method in zip(map(float, input().split()), (x.append, y.append))]

[item.append(item[0]) for item in (x, y)]

if count > 1:
    for i in range(int(count)):
        length += sqrt((x[i + 1] - x[i]) * (x[i + 1] - x[i]) + (y[i + 1] - y[i]) * (y[i + 1] - y[i]))

print(f'{length:0.2f}')