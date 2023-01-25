from math import ceil
print((lambda n, k: (ceil(n * 2.0 / k), ceil(n * 2.0 / n))[k > n])
(*map(lambda x: int(x), input().split())))