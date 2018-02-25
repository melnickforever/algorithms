from Sorting.abstractsorting import AbstractSorting


class InsertSorting(AbstractSorting):
    def sorting(self):
        for j in range(1, self.count):
            current = self.data[j]
            i = j - 1
            while i >= 0 and self.data[i] > current:
                self.data[i + 1] = self.data[i]
                i = i - 1
            self.data[i + 1] = current
