k, n = map(int, input().split())
cars = 0
a = list(map(int, input().split()))
for i in a:
    if i > k:
        cars += i - k
    elif cars != 0:
        if k - i > cars:
            cars = 0
        else:
            cars -= k - i
print(cars)
