from abc import ABC, abstractmethod


class AbstractSorting(ABC):

    @abstractmethod
    def sorting(self, data, count):
        pass
