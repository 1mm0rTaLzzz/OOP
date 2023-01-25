def main():
    l, h, w = map(float, input().split())
    g = 9.81 * 100
    if l / 2 >= h:
        print("butter")
        return

    time = (2 * (h - l / 2) / g) ** 0.5
    w = (lambda x: x - int(x))(w * time / 60)
    print(['bread', 'butter'][(0 <= w <= 1 / 4) or (3 / 4 <= w <= 1)])


if __name__ == '__main__':
    main()