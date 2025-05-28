class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if not directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} --> {self.graph[node]}")

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    g.print_graph()
