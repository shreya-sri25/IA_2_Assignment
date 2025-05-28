import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start):
        dist = [float("inf")] * self.V
        dist[start] = 0
        min_heap = [(0, start)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            for neighbor, weight in self.graph[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        return dist

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 5, 2)

    distances = g.dijkstra(0)
    for i in range(len(distances)):
        print(f"Distance from 0 to {i}: {distances[i]}")
