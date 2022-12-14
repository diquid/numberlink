class Node:
    def __init__(self, edge, mate, arc):
        self.edge = edge
        self.mate = mate
        self.arc = arc
        self.zero_child = None
        self.one_child = None

    def add_zero_child(self, child):
        self.zero_child = child

    def add_one_child(self, child):
        self.one_child = child


TERMINAL_ZERO = Node(None, None, 0)
TERMINAL_ONE = Node(None, None, 1)
