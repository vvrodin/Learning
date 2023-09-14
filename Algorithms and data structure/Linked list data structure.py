class Node:
    def __init__(self, args):
        if not args:
            self.data = None # в случае первоначального создания элементом списка
        else:
            self.data = args
        self.next_node = None
        self.previous_node = None
        return

    def __repr__(self):
        return str(list(self.data))


class linked_lists:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, *element):
        node = self.head
        while node is not None:
            if node.data == element:
                return node
            node = node.next_node
        return -1

    def count(self, *element):
        counter = 0
        node = self.head
        while node is not None:
            if node.data == element:
                counter += 1
            node = node.next_node
        return counter

    def show_list(self):
        res = ''
        node = self.head
        while node is not None:
            res += str(node) + ' - '
            node = node.next_node
        return res

    def __str__(self):
        return self.show_list()


class singly_linked_list(linked_lists):
    def push_back(self, *args):
        if self.head is None:
            self.head = Node(args)
            return None
        elif self.tail is None:
            self.head.next_node = Node(args)
            self.tail = self.head.next_node
            return None
        node = Node(args)
        self.tail.next_node = node
        self.tail = node

    def push_front(self, *args):
        node = Node(args)
        node.next_node = self.head
        self.head = node

    def remove(self, *element):
        node = self.head
        previous_node = -1
        while node.data != element and node.next_node is not None:
            previous_node = node
            node = node.next_node
        if node.data == element and node.next_node is None:
            previous_node.next_node = None
        if node.data != element and node.next_node is None:
            raise KeyError
        if previous_node == -1:
            self.head = self.head.next_node
            return
        previous_node.next_node = node.next_node
        return


class doubly_linked_list(linked_lists):
    def push_back(self, *args):
        if self.head is None:
            self.head = Node(args)
            return
        elif self.head.next_node is None:
            self.head.next_node = Node(args)
            self.head.next_node.previous_node = self.head
            self.tail = self.head.next_node
            return
        node = Node(args)
        node.previous_node = self.tail
        self.tail = node

    def push_front(self, *args):
        node = Node(args)
        self.head.previous_node = node
        node.next_node = self.head
        node.previous_node = None

    def remove(self, *element):
        node = self.head
        previous_node = -1
        while node.data != element and node.next_node is not None:
            previous_node = node
            node = node.next_node
        if node.data == element and node.next_node is None:
            self.tail = previous_node
            previous_node.next_node = None
            return
        if node.data != element and node.next_node is None:
            raise KeyError
        if previous_node == -1:
            self.head = self.head.next_node
            self.head.previous_node = None
            return
        previous_node.next_node = node.next_node
        node.next_node.previous_node = previous_node
        return
