k = int(input())
inv = [input() for i in range(k)]
res = k + 2 + ''.join(inv).count('+')
if res == 13:
    res += 1
print(res * 100)
