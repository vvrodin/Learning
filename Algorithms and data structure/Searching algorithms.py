class Searching:
    def __init__(self):
        self._counter = 0

    def comparison_counter(self, data, target, func):
        func(data, target)
        s = f'counter of comparison operations is {self._counter} for type {func}'
        self._counter = 0
        return s

    def sequential_search(self, list_, target):
        for i in range(len(list_)):
            self._counter += 1
            if list_[i] == target:
                return i
        return -1

    def sorted_sequential_search(self, list_, target):
        for i in range(len(list_)):
            self._counter += 1
            if list_[i] == target:
                return i
            if list_[i] > target:
                return -1
        return -1

    def binary_search(self, list_, target):
        counter = 0
        while len(list_) > 0:
            self._counter += 1
            if list_[len(list_) // 2] == target:
                counter += len(list_) // 2
                return counter
            if list_[len(list_) // 2] >= target:
                list_ = list_[: len(list_) // 2]
            elif list_[len(list_) // 2] < target:
                counter += len(list_) // 2 + 1
                list_ = list_[len(list_) // 2 + 1:]
        return -1