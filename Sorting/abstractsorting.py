from abc import ABC, abstractmethod
from random import randint


class AbstractSorting(ABC):

    def __init__(self, count):
        self.file_name = "sorting_report.txt"
        self.count = count
        self.range_start = 0
        self.range_end = 1000
        self.data = []
        self.init_data(count)

    def init_data(self, count):
        for i in range(count):
            self.data.append(randint(self.range_start, self.range_end))

    def save(self, title):
        file = open(self.file_name, "a")
        file.write("\n\n%s\n=======\n" % title)
        for item in self.data:
            file.write("%s," % item)
        file.close()

    @abstractmethod
    def sorting(self):
        pass
