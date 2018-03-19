from Sorting.Sorters.abstractsorting import AbstractSorting


class InsertSorting(AbstractSorting):
    def sorting(self, data, count):
        for j in range(1, count):
            current = data[j]
            i = j - 1
            while i >= 0 and data[i] > current:
                data[i + 1] = data[i]
                i = i - 1
            data[i + 1] = current

        return data
