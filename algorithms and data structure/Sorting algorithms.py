class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class binaryTree:
    def __init__(self):
        self.output = []
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if node.data == value:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False


    def append(self, object):
        if self.root is None:
            self.root = object
            return object

        s, p, fl_find = self.__find(self.root, None, object.data)

        if not fl_find and s:
            if object.data < s.data:
                s.left = object
            else:
                s.right = object
        return object

    def tree_sort(self, node):
        if node is None:
            return

        self.tree_sort(node.left)
        self.output.append(node.data)
        self.tree_sort(node.right)


class Sorting:
    def __init__(self):
        self._counter = 0

    def comparison_counter(self, data, *args, func):
        func(data, *args)
        func_name = str(func)[str(func).index("Sorting.") + 8: str(func).index("of")]
        s = f'counter of comparison operations is {self._counter} for {func_name}'
        self._counter = 0
        return s

    def __binary_search(self, list_input, target):
        list_ = list_input.copy()
        counter = 0
        while len(list_) > 0:
            self._counter += 1
            if list_[len(list_) // 2] >= target:
                list_ = list_[: len(list_) // 2]
            elif list_[len(list_) // 2] < target:
                counter += len(list_) // 2 + 1
                list_ = list_[len(list_) // 2 + 1:]
        return counter

    def insertion_sort_original(self, list_input):
        list_ = list_input.copy()
        for i in range(1, len(list_)):
            new_element = list_[i]
            location = i - 1
            while (location >= 0) and (new_element < list_[location]):
                self._counter += 1
                list_[location + 1], list_[location] = list_[location], list_[location + 1]
                location -= 1
        return list_

    def insertion_sort_with_binary_search(self, list_input):
        list_ = list_input.copy()
        for i in range(1, len(list_)):
            new_element = list_[i]
            location = i - 1
            if (location >= 0) and (new_element < list_[location]):
                self._counter += 1
                del list_[i]
                list_.insert(self.__binary_search(list_[:i], new_element), new_element)
        return list_

    def bubble_sort_original(self, list_input):
        list_ = list_input.copy()
        flag = True
        while flag:
            flag = False
            for i in range(1, len(list_)):
                self._counter += 1
                if list_[i] < list_[i - 1]:
                    list_[i], list_[i - 1] = list_[i - 1], list_[i]
                    flag = True
        return list_

    def bubble_sort_ver1(self, list_input):
        list_ = list_input.copy()
        flag = True
        last_swap = len(list_)
        while flag:
            flag = False
            for i in range(1, last_swap):
                self._counter += 1
                if list_[i] < list_[i - 1]:
                    list_[i], list_[i - 1] = list_[i - 1], list_[i]
                    last_swap = i
                    flag = True
        return list_

    def bubble_sort_ver2(self, list_input):
        list_ = list_input.copy()
        flag = True
        num = 0
        last_swap = len(list_)
        while flag:
            flag = False
            num += 1
            if num % 2 == 1:
                for i in range(1, last_swap):
                    self._counter += 1
                    if list_[i] < list_[i - 1]:
                        list_[i], list_[i - 1] = list_[i - 1], list_[i]
                        flag = True
            else:
                for i in range(last_swap - 1, 0, -1):
                    self._counter += 1
                    if list_[i - 1] > list_[i]:
                        list_[i], list_[i - 1] = list_[i - 1], list_[i]
                        flag = True
        return list_

    def bubble_sort_ver3(self, list_input):
        list_ = list_input.copy()
        flag = True
        num = 0
        last_swap = len(list_)
        while flag:
            flag = False
            num += 1
            if num % 2 == 1:
                for i in range(1, last_swap):
                    self._counter += 1
                    if list_[i] < list_[i - 1]:
                        list_[i], list_[i - 1] = list_[i - 1], list_[i]
                        last_swap = i
                        flag = True
            else:
                counter_rev = 0
                for i in range(last_swap - 1, 0, -1):
                    self._counter += 1
                    if list_[i - 1] > list_[i]:
                        counter_rev += 1
                        if counter_rev == 1:
                            last_swap = i
                        list_[i], list_[i - 1] = list_[i - 1], list_[i]
                        flag = True
        return list_

    def shell_sort_orig(self, list_input, steps=None):
        list_ = list_input.copy()
        if steps is None:
            steps = []
            while (increment := len(list_) // 2) > 0:
                steps.append(increment)
                increment //= 2
        for increment in steps:
            for i in range(increment):
                output = []
                for j in range(i, len(list_), increment):
                    output.append(list_[j])
                output = self.insertion_sort_original(output)
                t = -1
                for j in range(i, len(list_), increment):
                    t += 1
                    list_[j] = output[t]
            increment //= 2
        return list_

    def shell_sort_with_binary_search(self, list_input, steps=None):
        list_ = list_input.copy()
        if steps is None:
            steps = []
            while (increment := len(list_) // 2) > 0:
                steps.append(increment)
                increment //= 2
        for increment in steps:
            for i in range(increment):
                output = []
                for j in range(i, len(list_), increment):
                    output.append(list_[j])
                output = self.insertion_sort_with_binary_search(output)
                t = -1
                for j in range(i, len(list_), increment):
                    t += 1
                    list_[j] = output[t]
            increment //= 2
        return list_

    def radix_sort(self, list_input):
        list_ = list_input.copy()
        number_digit = 1
        mx_len = len(str(max(list_, key=lambda x: len(str(x)))))
        while number_digit <= mx_len:
            bucket = [[] for _ in range(10)]
            for i in list_:
                num = str(i)
                if len(num) < number_digit:
                    bucket[0].append(i)
                else:
                    bucket[int(num[-number_digit])].append(i)
            list_.clear()
            for i in bucket:
                list_.extend(i)
            number_digit += 1
        return list_

    def heap_sort(self, list_input):
        list_ = list_input.copy()
        tree = binaryTree()

        for i in list_:
            tree.append(Node(i))
        tree.tree_sort(tree.root)
        return tree.output

    def __merge_lists(self, list_A, list_B):
        output = []
        index_A = index_B = 0
        while len(list_A) != index_A and len(list_B) != index_B:
            self._counter += 1
            if list_A[index_A] > list_B[index_B]:
                output.append(list_B[index_B])
                index_B += 1
            else:
                output.append(list_A[index_A])
                index_A += 1
        if len(list_A) == index_A:
            output.extend(list_B[index_B:])
        else:
            output.extend(list_A[index_A:])
        return output

    def merge_sort(self, list_input):
        list_ = list_input.copy()
        if len(list_) != 1:
            list_A = self.merge_sort(list_[:len(list_) // 2])
            list_B = self.merge_sort(list_[len(list_) // 2:])
            return self.__merge_lists(list_A, list_B)
        else:
            return list_

    def quick_sort_original(self, list_input):
        list_ = list_input.copy()
        if len(list_) > 1:
            pivot = list_[0]
            list_A = self.quick_sort_original(list(filter(lambda x: x < pivot, list_)))
            list_B = self.quick_sort_original(list(filter(lambda x: x > pivot, list_)))
            self._counter += len(list_) - 1
            return list_A + [pivot] + list_B
        else:
            return list_

    def quick_sort_with_mid_pivot(self, list_input):
        list_ = list_input.copy()
        if len(list_) > 1:
            pivot = list_[len(list_) // 2]
            list_A = self.quick_sort_with_mid_pivot(list(filter(lambda x: x < pivot, list_)))
            list_B = self.quick_sort_with_mid_pivot(list(filter(lambda x: x > pivot, list_)))
            self._counter += len(list_) - 1
            return list_A + [pivot] + list_B
        else:
            return list_

    def selection_sort(self, list_input):
        list_ = list_input.copy()
        for i in range(0, len(list_) - 1):
            min = i
            for j in range(i + 1, len(list_)):
                if list_[j] < list_[min]:
                    min = j
            min_value = list_[min]
            list_[min] = list_[i]
            list_[i] = min_value
        return list_


  #бинарная сортировка шелла менее эффективна чем обычная сортировка шелла
