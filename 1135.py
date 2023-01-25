n = int(input())
s, k = str(), 0
while len(s) != n:
    s += input()

_, __ = 0, 0
count = 0

for ch in s:
    if ch == '<':
        count += _ - __
        _, __ = _ + 1, __ + 1
    elif ch == '>':
        _ += 1

print(count)