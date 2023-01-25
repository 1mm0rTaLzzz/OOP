from typing import List, NoReturn
from abc import ABC, abstractmethod


class Sort(ABC):
    @abstractmethod
    def sorted(self, data: List[object]) -> NoReturn:
        pass


class BitwiseSort(Sort):

    @staticmethod
    def __set_bit(digit: int, n: int) -> int:
        digit |= 1 << n
        return digit

    def sorted(self, data: List[int]):
        bits = 0b0
        for item in data:
            bits = self.__set_bit(bits, item)
        data.clear()

        for index, item in enumerate(map(int, list(bin(bits)[2:])[::-1])):
            if item == 1:
                data.append(index)


def main() -> NoReturn:
    n = int(input())
    power = 2 ** n
    repeat_elements = {}
    for _ in range(power):
        key = input().split()[-1]
        repeat_elements[key] = repeat_elements.get(key, 0) + 1

    repeat_values = list(repeat_elements.values())
    BitwiseSort().sorted(repeat_values)
    max_repeat = repeat_values[-1]
    for i in range(n):
        power //= 2
        if max_repeat > power:
            print(i)
            break
    else:
        print(n)


if __name__ == '__main__':
    main()