s = int(input())
if s == 0:
    print('10')
elif s < 10:
    print(s)
else:
    out = ""
    for i in range(9, 1, -1):
        while s % i == 0:
            s /= i
            out = str(i) + out
    if s > 1:
        print('-1')
    else:
        print(out)
