from typing import List, NoReturn
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Sort(ABC):
    @abstractmethod
    def sorted(self, data: List[object]) -> NoReturn:
        pass


class QuickSort(Sort):
    def sorted(self, data: List[object]):
        data.sort()


@dataclass
class Main(object):
    count_requests: int
    data: List[int]
    sort: Sort

    def __get_request(self, index: int):
        return self.data[index - 1]

    def main(self):
        self.sort.sorted(self.data)
        for _ in range(self.count_requests):
            print(self.__get_request(int(input())))


if __name__ == '__main__':
    Main(
        data=[int(item) for item in [input() for _ in range(int(input()) + 1)] if item.isdigit()],
        count_requests=int(input()),
        sort=QuickSort(),
    ).main()