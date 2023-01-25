L, T, va, vb = map(int, input().split())
n = int(input())
t = [0] * 2
while n:
    n -= 1
    i, _, d = map(int, input().split())
    if 0 <= (i - 1) <= 1:
        t[i - 1] += d
print(int((va * (T - t[0]) + vb * (T - t[1]))/L))