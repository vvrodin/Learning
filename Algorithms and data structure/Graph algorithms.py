class Node:
    def __init__(self, num):
        self.num = num
        self.links = {}

    def add_link(self, node, weight=0):
        self.links[node.get_num()] = (node, weight)

    def get_num(self):
        return self.num

    def __str__(self):
        return f'Node({self.get_num() + 1})'


class Graph:
    def __init__(self):
        self.nodes = {}

    def get_node(self, num):
        return self.nodes[num]

    def initial_generation(self, matrix, node=Node(0)):
        dict = {}
        self.nodes[node.get_num()] = node
        for i in range(len(matrix[0])):
            if matrix[node.get_num()][i] != 'inf':
                dict[i] = matrix[node.get_num()][i]  # находим все смежные ребра и их вес
        for i in dict.keys():
            node1 = self.nodes.get(i, Node(i))
            node.add_link(node1, weight=dict[i])  # создаем  оринетированное ребро
            if i not in self.nodes.keys():
                self.initial_generation(matrix, node=node1)  # если узел встретился впервые продолжаем обход в глубину
        if node.get_num() == 0:  # после первого обхода проверяем граф на связность
            missed = set(list(range(len(matrix[0])))).difference(set(self.nodes.keys()))
            while len(missed) != 0:
                self.initial_generation(matrix, node=Node(list(missed)[0]))
                missed = set(list(range(1, len(matrix[0])))).difference(set(self.nodes.keys()))

    def depth_first_traversal(self, start_node):
        nodes = start_node.links
        for i in sorted(nodes.keys()):
            self.depth_first_traversal(start_node=nodes[i][0])
        return

    def show_graph(self, node=None, st='', visited=[]):  # добавить обход по всем несвязным элементам
        nodes = node.links
        visited.append(node.get_num())
        st += f'[{str(node.get_num())}]-'
        for i in sorted(nodes.keys()):
            if i not in visited:
                st += self.show_graph(node=nodes[i][0], visited=visited)
        return st