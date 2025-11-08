import heapq
import math

class Graph:
    def __init__(self):
        self.vertices = []  # List of vertex names
        self.adj_matrix = []  # 2D matrix of weights

    def add_vertex(self, vertex_name):
        """Add a vertex to the graph if it doesn't exist."""
        if vertex_name not in self.vertices:
            self.vertices.append(vertex_name)
            # Expand adjacency matrix for the new vertex
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(None)
            self.adj_matrix.append([None] * size)

    def add_edge(self, vertex1, vertex2, weight):
        """Add an undirected weighted edge between vertex1 and vertex2."""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        i = self.vertices.index(vertex1)
        j = self.vertices.index(vertex2)

        self.adj_matrix[i][j] = weight
        self.adj_matrix[j][i] = weight

    def _dijkstra(self, start):
        n = len(self.vertices)
        distances = [math.inf] * n
        previous = [None] * n
        visited = [None] * n

        if start not in self.vertices:
            return None, None

        start_index = self.vertices.index(start)
        distances[start_index] = 0

        pq = [(0, start_index)]

        while pq:
            curr, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True

            for v in range(n):
                weight = self.adj_matrix[u][v]
                if weight is not None and not visited[v]:
                    new_dist = curr + weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        previous[v] = u
                        heapq.heappush(pq, (new_dist, v))

        return distances, previous

    def shortest_path(self, v1, v2):
        distances, previous = self._dijkstra(v1)
        if distances is None or previous is None or v2 not in self.vertices:
            return None

        end_index = self.vertices.index(v2)
        if distances[end_index] == math.inf:
            return None

        path = []
        curr = end_index
        while curr is not None:
            path.insert(0, self.vertices[curr])
            curr = previous[curr]

        return path
    def shortest_distance(self, v1, v2):
        distances, _ = self._dijkstra(v1)
        if distances is None or v2 not in self.vertices:
            return None
        end_index = self.vertices.index(v2)
        return distances[end_index] if distances[end_index] != math.inf else None

def print_adjacency_matrix(graph):
    """Print the adjacency matrix with vertex names."""
    vertices = graph.vertices
    print("Adjacency Matrix:")

    # Print header row
    print("    ", end="")
    for v in vertices:
        print(f"{v:>5}", end="")
    print()

    # Print each row with vertex labels
    for i, row in enumerate(graph.adj_matrix):
        print(f"{vertices[i]:>4}", end=" ")
        for weight in row:
            value = "-" if weight is None else str(weight)
            print(f"{value:>5}", end="")
        print()

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "D", 4)
    g.add_edge("B", "D", 7)

    print_adjacency_matrix(g)

    path = g.shortest_path("A", "D")
    distance = g.shortest_distance("A", "D")

    print("\nShortest path from A to D:", path)
    print("Shortest distance from A to D:", distance)


