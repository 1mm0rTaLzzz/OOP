from math import ceil
(lambda n, step, digits: [print(*[x.rjust(4) for x in digits[i::ceil(n / step)]], sep='') for i in range(ceil(n / step))])(*map(int, input().split()), input().split())