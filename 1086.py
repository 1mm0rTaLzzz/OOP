from typing import List


def primes(n: int) -> List[int]:
    digits = list(range(n + 1))
    digits[1], i = 0, 2
    while i <= n:
        if digits[i] != 0:
            j = i + i
            while j <= n:
                digits[j] = 0
                j = j + i
        i += 1
    digits = set(digits)
    digits.remove(0)

    return list(digits)


n = int(input())
digits = sorted(primes(165550))
[print(digits[int(input()) - 1]) for i in range(n)]
