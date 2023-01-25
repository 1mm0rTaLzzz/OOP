def main(n: int) -> str:
    count = 0
    divided = 2
    while divided * divided <= n:
        if n % divided == 0:
            count += 1
            n //= divided
            if count > 20:
                return 'No'
        else:
            divided += 1
            if divided > 2 * 10 ** 6:
                return 'No'
    if n > 1:
        count += 1
    return ['No', 'Yes'][count == 20]


if __name__ == '__main__':
    print(main(int(input())))