from typing import List, NoReturn
from abc import ABC, abstractmethod
from random import randint
from dataclasses import dataclass


def binSearch(array: List[int], search_item: int):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if search_item < array[middle]:
            end = middle - 1
        elif search_item > array[middle]:
            start = middle + 1
        elif array[middle] == search_item:
            return True

    return False


class Sort(ABC):
    @abstractmethod
    def sorted(self, data: List[object]) -> NoReturn:
        pass


class BogoSort(Sort):

    @staticmethod
    def __correct(data: List[object]):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                return False
        return True

    @staticmethod
    def __shuffle(data: List[object]):
        index_i = randint(0, len(data))
        index_j = randint(0, len(data))
        data[index_i], data[index_j] = data[index_j], data[index_i]

    def sorted(self, data: List[object]):
        while not self.__correct(data):
            self.__shuffle(data)


@dataclass
class Main(object):
    arrays: List[List[int]]
    sort: Sort

    def main(self):
        for array in self.arrays:
            self.sort.sorted(array)

        count = 0
        for item in (set(self.arrays[0] + self.arrays[1] + self.arrays[2])):
            count_item = 0
            for array in self.arrays:
                if binSearch(array, item):
                    count_item += 1
                    continue
            if count_item == 3:
                count += 1

        print(count)


if __name__ == '__main__':

    arrays = []
    for _ in range(3):
        input()
        arrays.append(list(map(int, input().split())))

    Main(
        arrays=arrays,
        sort=BogoSort(),
    ).main()