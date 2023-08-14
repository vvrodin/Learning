class Node:
    def __init__(self, *args, first_init=False):
        if first_init:
            self.data = None
        else:
            self.data = list(*args)
        self.next_node = None
        self.previous_node = None
        return

    def __str__(self):
        return str(self.data)


class linked_lists:
    def __init__(self):
        self.head = None

    def find(self, *element):
        element = list(element)
        node = self.head
        while node.data != element and node.next_node is not None:
            node = node.next_node
        if node.data == element:
            return node
        if node.data != element:
            return -1

    def count(self, *element):
        counter = 0
        element = list(element)
        node = self.head
        while node.next_node is not None:
            if node.data == element:
                counter += 1
            node = node.next_node
        if node.data == element:
            counter += 1
        return counter

    def show_list(self):
        node = self.head
        while node.next_node is not None:
            print(node, end=' - ')
            node = node.next_node
        print(node)


class singly_linked_list(linked_lists):
    def __init__(self):
        super().__init__()
        self.head = Node(None, first_init=True)
        self.head.next_node = Node(None, first_init=True)

    def push_back(self, *args):
        args = list(args)
        if self.head.data is None:
            self.head.data = args
            return None
        elif self.head.next_node.data is None:
            self.head.next_node.data = args
            return None
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        node.next_node = Node(args)

    def push_front(self, *args):
        args = list(args)
        node = Node(args)
        node.next_node = self.head
        self.head = node

    def remove(self, *element):
        element = list(element)
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
    def __init__(self):
        super().__init__()
        self.head = Node(None, first_init=True)
        self.head.previous_node = None
        self.head.next_node = Node(None, first_init=True)
        self.head.next_node.previous_node = self.head
        self.tail = self.head.next_node

    def push_back(self, *args):
        args = list(args)
        if self.head.data is None:
            self.head.data = args
            return None
        elif self.head.next_node.data is None:
            self.head.next_node.data = args
            return None
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        node.next_node = Node(args)
        node.next_node.previous_node = node
        self.tail = node.next_node

    def push_front(self, *args):
        args = list(args)
        node = Node(args)
        node.next_node = self.head
        self.head = node
        self.head.next_node.previous_node = node
        self.head.previous_node = None

    def remove(self, *element):
        element = list(element)
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
