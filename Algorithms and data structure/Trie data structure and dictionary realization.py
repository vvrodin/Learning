class Node:
    def __init__(self, *args, symbol):
        self.symbol = symbol
        if not args:
            Node.data = None
            Node.is_key = False
        else:
            Node.data = list(*args)
        self.next_nodes = []

    def add_data(self, *args):
        self.data = args

    def __str__(self):
        return f'Node({self.symbol})'


class Trie:
    def __init__(self):
        self.head = Node(symbol='')

    def __key_validation(self, key):
        if type(key) != str:
            raise KeyError
        key = key.strip()
        if key == '':
            raise KeyError

    def __find_node(self, key, add=False, previous=False):
        node = self.head
        i = 0
        flag = True
        previous_node = node
        while flag and i < len(key):
            symbol = key[i]
            flag = False
            for j in node.next_nodes:
                if symbol == j.symbol:
                    flag = True
                    previous_node = node
                    node = j
            if not flag and add:
                temp = Node(symbol=symbol)
                node.next_nodes.append(temp)
                node = temp
                flag = True
            i += 1
        if not flag:
            return -1
        elif flag and previous:
            return node, previous_node
        elif flag:
            return node

    def add(self, key, data):
        self.__key_validation(key)
        node = self.__find_node(key, add=True)
        node.data = data

    def find(self, key):
        self.__key_validation(key)
        node = self.__find_node(key)
        if node == -1:
            return -1
        else:
            return node.data

    def remove(self, key):
        self.__key_validation(key)
        node, previous_node = self.__find_node(key, previous=True)
        if node == -1:
            raise KeyError
        elif not node.next_nodes:
            previous_node.pop(previous_node.index(node))
        else:
            node.data = None

    def __show_trie(self, node, s=''):
        s += node.symbol
        if node.next_nodes:
            if node.data:
                r = f"'{s}': {node.data}, "
                for j in node.next_nodes:
                    r += self.__show_trie(j, s)
                return r
            else:
                r = ''
                for j in node.next_nodes:
                    r += self.__show_trie(j, s)
                return r
        else:
            return f"'{s}': {node.data}, "


class dictionary(Trie):
    def __str__(self):
        return '{' + self.__show_trie(self.head) + '}'

    def __getitem__(self, item):
        return self.find(item)

    def __setitem__(self, key, value):
        return self.add(key=key, data=value)

    def __delitem__(self, key):
        self.remove(key)