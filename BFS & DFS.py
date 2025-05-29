from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:", end=" ")

    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

if __name__ == "__main__":
    bfs(graph, 'A')
    dfs(graph, 'A')
