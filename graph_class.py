class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, x, y):
        self.vertices.add(x)
        self.vertices.add(y)
        self.edges.append([x, y])