class Node:
    def __init__(self, args):
        if not args:
            self.data = None # в случае первоначального создания элементом списка
        else:
            self.data = args
        self.next_node = None
        self.previous_node = None
        return

    def __str__(self):
        return str(list(self.data))


class linked_lists:
    def __init__(self):
        self.head = None
        self.tail = None

    def show_list(self):
        res = ''
        node = self.head
        while node is not None:
            res += str(node) + ' - '
            node = node.next_node
        return res

    def __str__(self):
        return self.show_list()


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


class FIFO_queue(linked_lists):
    def push(self, *args):
        if self.head is None:
            self.head = Node(args)
        elif self.head.next_node is None:
            node = self.head
            self.head = Node(args)
            self.head.next_node = node
            self.head.next_node.previous_node = self.head
            self.tail = self.head.next_node
        else:
            node = self.head
            self.head = Node(args)
            self.head.next_node = node
            self.head.next_node.previous_node = self.head

    def pop(self):
        if self.head is None:
            return
        res = self.tail
        self.tail = self.tail.previous_node
        self.tail.next_node = None
        return res

    def empty(self):
        return self.head is None

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next_node
        return size


class LIFO_queue(linked_lists):  #Stack
    def push(self, *args):
        if self.head is None:
            self.head = Node(args)
        elif self.head.next_node is None:
            self.head.next_node = Node(args)
            self.head.next_node.previous_node = self.head
            self.tail = self.head.next_node
        else:
            node = Node(args)
            node.previous_node = self.tail
            self.tail.next_node = node
            self.tail = self.tail.next_node

    def pop(self):
        if self.head is None:
            return
        res = self.tail
        self.tail = self.tail.previous_node
        self.tail.next_node = None
        return res

    def peek(self):
        if self.head is not None and self.tail is None:
            return self.head
        return self.tail

    def empty(self):
        return self.head is None

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next_node
        return size
