n = int(input())
s = 0
for i in range(1, abs(n) + 1):
    s = s + i
if(n > 0):
    print(s)
elif n == 0:
    print(1)
else:
    s = "-" + str(s - 1)
    print(int(s))