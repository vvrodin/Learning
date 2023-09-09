class Node:
    def __init__(self, num, dictionary_links):
        self.num = num


class Graph:
    def __init__(self):
        self.nodes = []

    def validation(self, matrix, directed=False, node=0):
        if not directed:
            dict = {}
            self.nodes.append(node)
            for i in range(len(matrix[0])):
                if matrix[node][i] == 1:
                    dict[i] = 1
            for i in
            self.validation(self, matrix, node=)








matrix = [[0, 1, 1], [1, 0, 1], [0, 1, 1]]
G = Graph()
G.validation(matrix)
print(G.nodes)