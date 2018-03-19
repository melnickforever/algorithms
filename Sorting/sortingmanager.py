from Sorting.Sorters.insertsorting import InsertSorting
from random import randint
from datetime import datetime


class SortingManager:
    DATA_SEPARATOR = ","
    DATA_FORMAT = "%s"
    DATA_RESULT_PATH = "Results/"

    def __init__(self, count):
        self.source_filename = self.DATA_RESULT_PATH + "sourceData.txt"
        self.count = count
        self.range_start = 0
        self.range_end = 10
        self.data = []
        self.init()

    def init(self):
        file = open(self.source_filename, "w");
        for i in range(self.count):
            current_item = randint(self.range_start, self.range_end)
            if i + 1 == self.count:
                file.write(self.DATA_FORMAT % current_item)
            else:
                file.write((self.DATA_FORMAT + self.DATA_SEPARATOR) % current_item)
        file.close()

    def read(self):
        with open(self.source_filename) as f:
            original_data = f.read()
        f.close()
        return original_data.split(self.DATA_SEPARATOR)

    def save(self, sorted_data, exec_time, file_name):
        with open(self.DATA_RESULT_PATH + file_name, "w") as f:
            f.write(("Execution time:  " + self.DATA_FORMAT + " sec.\n\n") % exec_time)
            f.write(self.DATA_SEPARATOR.join(sorted_data))
        f.close()

    def sort(self, sorter_object):
        original_data = self.read()
        start_time = datetime.now()
        sorted_data = sorter_object.sorting(original_data, self.count)
        exec_time = datetime.now() - start_time
        result_file = sorter_object.__class__.__name__ + ".txt"
        self.save(sorted_data, exec_time, result_file)


obj = SortingManager(100)
obj.sort(InsertSorting())
