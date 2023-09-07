class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class binaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if node.data == value:
            return node, parent, True

        if value < node.data:  # если значение оказывается меньше чем в текущем узле
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:  # если значение оказывается больше чем в текущем узле
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False  # выполняется в случае если нашли узел, у которого нет нужного потомка

    def append(self, object):
        if self.root is None:
            self.root = object
            return object
        s, parent, fl_find = self.__find(self.root, None, object.data)
        if not fl_find and s:
            if object.data < s.data:
                s.left = object
            else:
                s.right = object
            self.size += 1
        return object

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        if p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, parent)
        return node, parent

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)
        if not fl_find:
            return None
        elif s.left is None and s.right is None:
            self.size -= 1
            p.left = None
        elif s.left is None or s.right is None:
            self.size -= 1
            self.__del_one_child(s, p)
        else:
            self.size -= 1
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def size(self):
        return self.size

    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
            if x.left:
                vn += [x.left]
            if x.right:
                vn += [x.right]
            print()
            v = vn


class my_set(binaryTree):
    def add(self, data):
        self.append(data)

    def difference(self, set1):
        pass

    def symmetric_difference(self):
        pass

    def intersection(self):
        pass

    def issubset(self, set1):
        if self.size >= set1.size():
            return False
        if

    def isupperset(self):
        pass

    def union(self):
        pass
