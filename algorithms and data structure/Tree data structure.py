class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class binaryTree:
    def __init__(self):
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
            p.left = None

        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

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


tr = binaryTree()
v = [7, 4, 9, 2, 5, 8]
for i in v:
    tr.append(Node(i))

tr.show_wide_tree(tr.root)