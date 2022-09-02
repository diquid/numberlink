class Graph:
    def __init__(self):
        self.verts = set()
        self.edges = []

    def add_edge(self, x, y):
        self.verts.add(x)
        self.verts.add(y)
        self.edges.append([x, y])