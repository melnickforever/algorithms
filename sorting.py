from Sorting.sortingmanager import SortingManager
from Sorting.Sorters.insertsorting import InsertSorting

min = 0
max = 10
experiments = (10, 100, 1000, 10000)

for count in experiments:
    manager = SortingManager(count, min, max, True)
    sorter = InsertSorting()
    manager.sort(sorter)
    del sorter
    del manager