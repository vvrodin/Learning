class Node:
    def __init__(self, *args, symbol):
        self.symbol = symbol
        if not args:
            Node.data = None
            Node.is_key = False
        else:
            Node.data = list(*args)
            Node.is_key = True
        self.next_nodes = []

    def __str__(self):
        return f'node({self.symbol})'


class Trie:
    def __init__(self):
        self.head = Node(symbol='')

    def __key_validation(self, key):
        if type(key) != str:
            raise KeyError
        key = key.strip()
        if key == '':
            raise KeyError

    def __find_node(self, key, if_not=False):
        node = self.head
        for i in range(len(key)):
            symbol = key[i]
            if symbol in [t.symbol for t in node.next_nodes]:
                for j in node.next_nodes:
                    if j.symbol == symbol:
                        node = j
                if i == len(key) - 1:
                    return node
            else:
                if if_not:
                    return -1
                if i == len(key) - 1:
                    temp = Node(symbol=symbol)
                    node.next_nodes.append(temp)
                    node = temp
                    return node
                else:
                    temp = Node(symbol=symbol)
                    node.next_nodes.append(temp)
                    node = temp

    def add(self, key, data):
        self.__key_validation(key)
        node = self.__find_node(key)
        node.data = data

    def find(self, key):
        self.__key_validation(key)
        node = self.__find_node(key)
        if node == -1:
            return -1
        else:
            return node.data

    def __show_trie(self, node, s=''):
        s += node.symbol
        if node.next_nodes:
            if node.data:
                r = f"'{s}' : {node.data}; "
                for j in node.next_nodes:
                    r += self.__show_trie(j, s)
                return r
            else:
                r = ''
                for j in node.next_nodes:
                    r += self.__show_trie(j, s)
                return r
        else:
            return f"'{s}' : {node.data}; "

    def __str__(self):
        return self.__show_trie(self.head)

    def __getitem__(self, item):
        return self.find(item)

    def __setitem__(self, key, value):
        return self.add(key=key, data=value)
