from math import ceil
from typing import List, NoReturn
from abc import ABC, abstractmethod


class Sort(ABC):
    @abstractmethod
    def sorted(self, data: List[object]) -> NoReturn:
        pass


class BubbleSort(Sort):
    def sorted(self, data: List[object]):
        for _ in data:
            for indexI, itemI in enumerate(data[:-1]):
                if itemI > data[indexI + 1]:
                    data[indexI], data[indexI + 1] = data[indexI + 1], data[indexI]


class Groups(object):
    def __init__(self, size: int, count_people: List[int]):
        self.__size = size
        self.__count_people = count_people

    def get_size(self) -> int:
        return self.__size

    def get_count_people(self) -> List[int]:
        return self.__count_people


class CountingOfVotes(object):
    @staticmethod
    def count(group: Groups, sort: Sort) -> int:
        data = group.get_count_people()
        sort.sorted(data)
        return sum(map(lambda x: ceil(x / 2), data[:ceil(group.get_size() / 2)]))


def main() -> NoReturn:
    print(CountingOfVotes.count(
        group = Groups(
            size = int(input()),
            count_people = list(map(int, input().split()))
        ),
        sort = BubbleSort(),
    ))


if __name__ == '__main__':
    main()