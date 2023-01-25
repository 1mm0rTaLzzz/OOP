n, k = map(int, input().split())
digits = [int(input()) for _ in range(n)]
print(*([digits[i % n] for i in range(k, k + 10)]), sep='')