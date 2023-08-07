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

    def recurtree_sort(self, node):
        if node is None:
            return

        self.recurtree_sort(node.left)
        self.output.append(node.data)
        self.recurtree_sort(node.right)


class Sorting:
    def __init__(self):
        self._counter = 0

    def comparison_counter(self, data, func):
        func(data)
        t = self._counter
        self._counter = 0
        return t

    def __binary_search(self, list_, target):
        counter = 0
        while len(list_) > 0:
            self._counter += 1
            if list_[len(list_) // 2] >= target:
                list_ = list_[: len(list_) // 2]
            elif list_[len(list_) // 2] < target:
                counter += len(list_) // 2 + 1
                list_ = list_[len(list_) // 2 + 1:]
        return counter

    def insertionSort_orig(self, list_):
        for i in range(1, len(list_)):
            newElement = list_[i]
            location = i - 1
            self._counter += 1
            while (location >= 0) and (newElement < list_[location]):
                self._counter += 1
                list_[location + 1], list_[location] = list_[location], list_[location + 1]
                location -= 1
        return list_

    def insertionSort_ver1(self, list_):
        for i in range(1, len(list_)):
            newElement = list_[i]
            location = i - 1
            self._counter += 1
            if (location >= 0) and (newElement < list_[location]):
                self._counter += 1
                del list_[i]
                list_.insert(self.__binary_search(list_[:i], newElement), newElement)
        return list_

    def BubbleSort_orig(self, list):
        flag = True
        while flag:
            flag = False
            for i in range(1, len(list)):
                self._counter += 1
                if list[i] < list[i - 1]:
                    list[i], list[i - 1] = list[i - 1], list[i]
                    flag = True
        return list

    def BubbleSort_ver1(self, list_):
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

    def BubbleSort_ver2(self, list_):
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

    def BubbleSort_ver3(self, list_):
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

    def Shellsort_orig(self, list_):
        increment = len(list_) // 2
        while increment > 0:
            for i in range(increment):
                output = []
                for j in range(i, len(list_), increment):
                    output.append(list_[j])
                output = self.insertionSort_orig(output)
                t = -1
                for j in range(i, len(list_), increment):
                    t += 1
                    list_[j] = output[t]
            increment //= 2
        return list_

    def Shellsort_ver1(self, list_):
        increment = len(list_) // 2
        while increment > 0:
            for i in range(increment):
                output = []
                for j in range(i, len(list_), increment):
                    output.append(list_[j])
                output = self.insertionSort_ver1(output)
                t = -1
                for j in range(i, len(list_), increment):
                    t += 1
                    list_[j] = output[t]
            increment //= 2
        return list_

    def RadixSort(self, list_):  # добавить сounter
        t = 1
        mx_len = 1
        while t <= mx_len:
            bucket = [[] for _ in range(10)]
            for i in list_:
                if len(str(i)) > mx_len:
                    mx_len = len(str(i))
                num = str(i)
                if len(num) < t:
                    bucket[0].append(i)
                else:
                    bucket[int(num[-t])].append(i)
            list_.clear()
            for i in bucket:
                list_.extend(i)
            t += 1
        return list_

    def HeapSort(self, list_):
        Tree = binaryTree()

        for i in list_:
            Tree.append(Node(i))
        Tree.recurtree_sort(Tree.root)
        return Tree.output




