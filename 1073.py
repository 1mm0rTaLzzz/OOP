class Digit(object):
    def __init__(self, digit: int):
        self.digit = digit

    def __add__(self, other: int):
        self.digit += other
        return True

    def __str__(self):
        return f'{self.digit}'


count = Digit(0)


def find_squares(n, squares_amount):
    global count
    if squares_amount == 1:
        return (False, count.__add__(n ** 0.5 == int(n ** 0.5)))[n ** 0.5 == int(n ** 0.5)]

    square = 1
    while square ** 2 < n:
        x = find_squares(n - square ** 2, squares_amount - 1)
        if x:
            return (True, count.__add__(x))[0]
        square += 1
    return False


att = [1, 1, 2, 3]
num = int(input())
for index in range(att[num % 4], 5):
    squares = (find_squares(num, index))
    if squares:
        print(count)
        break
