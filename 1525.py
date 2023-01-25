dirct = [0] * 512
dim = [0] * 512
res, maxx, minn, a, p = [0] * 3, [0] * 3, [0] * 3, [0] * 3, [0] * 3
dirct[ord('r')], dirct[ord('u')], dirct[ord('f')] = 1, 1, 1
dirct[ord('l')], dirct[ord('d')], dirct[ord('b')] = -1, -1, -1
dim[ord('r')], dim[ord('l')] = 0, 0
dim[ord('u')], dim[ord('d')] = 1, 1
dim[ord('f')], dim[ord('b')] = 2, 2

n, m, k = map(int, input().split())
d = [n, m, k]
s = input()
for c in s:
    D = dim[ord(c)]
    p[D] += dirct[ord(c)]
    maxx[D] = max(maxx[D], p[D])
    minn[D] = min(minn[D], p[D])

for _ in range(3):
    a[_] = max((d[_] + minn[_]) - maxx[_], 1)
print(a[0] * a[1] * a[2])
