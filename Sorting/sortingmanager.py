from Sorting.insertsorting import InsertSorting


class SortingManager:
    def action(self, sorter):
        # flush report file
        file = open(sorter.file_name, "w");
        file.close()
        # sorting
        sorter.save("Original sequence")
        sorter.sorting()
        sorter.save("Sorted sequence")


obj = SortingManager()
obj.action(InsertSorting(100))
