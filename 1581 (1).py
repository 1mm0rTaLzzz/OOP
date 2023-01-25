n = int(input())
digits = list(map(str, (input() + ' END').split()))

count = 1
for index in range(n):
    if digits[index] == digits[index + 1]:
        count += 1
    else:
        print(count, digits[index], end=" ")
        count = 1