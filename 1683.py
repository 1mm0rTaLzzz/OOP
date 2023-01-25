n, a = int(input()), list()
while n != 1:
    n = int((n + 1) / 2)
    a.append(n)
print(len(a))
print(*map(int, a), end=' ')