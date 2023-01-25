dict = {}

for _ in range(6):
    name, item, price = input(), input(), int(input())
    if item in dict:
        dict[item].append(price)
    else:
        dict[item] = [price]

price, c, name = int(), int(), ''
for item in dict.keys():
    low = min(dict[item])
    num = len(dict[item])
    if num > c:
        c = num
        price = low
        name = item
    elif num == c:
        if low < price:
            c = num
            price = low
            name = item

print(name)
