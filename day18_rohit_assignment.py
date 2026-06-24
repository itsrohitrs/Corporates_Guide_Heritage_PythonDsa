# =====================================================
# Name: Rohit Kumar Singh
# Assignment: DSA Module 5
# Topic: Graphs, BFS and DFS
# File Name: day18_rohit_assignment.py
# =====================================================

from collections import deque


class Graph:

    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    # =================================================
    # Part A
    # 1. Add Vertex
    # =================================================
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    # =================================================
    # Part A
    # 2. Add Edge
    # =================================================
    def add_edge(self, u, v):

        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].append(v)

        if not self.directed:
            self.adj_list[v].append(u)

    # =================================================
    # Part A
    # 3. Display Graph
    # =================================================
    def display(self):

        print("\nAdjacency List:")

        for vertex in sorted(self.adj_list):
            print(f"{vertex} -> {self.adj_list[vertex]}")

    # =================================================
    # Part B
    # 4. BFS
    # =================================================
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)

        order = []

        while queue:

            current = queue.popleft()

            order.append(current)

            for neighbor in self.adj_list[current]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # =================================================
    # Part C
    # 8. DFS using Recursion
    # =================================================
    def dfs(self, start):

        visited = set()
        order = []

        def dfs_recursive(node):

            visited.add(node)

            order.append(node)

            for neighbor in self.adj_list[node]:

                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)

        return order

    # =================================================
    # Bonus 2
    # Path Exists
    # =================================================
    def has_path(self, src, dest):

        visited = set()
        queue = deque([src])

        visited.add(src)

        while queue:

            current = queue.popleft()

            if current == dest:
                return True

            for neighbor in self.adj_list[current]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    queue.append(neighbor)

        return False

    # =================================================
    # Bonus 3
    # Within K Connections
    # =================================================
    def within_k_connections(self, start, k):

        visited = set([start])

        queue = deque([(start, 0)])

        result = []

        while queue:

            node, distance = queue.popleft()

            if 0 < distance <= k:
                result.append(node)

            if distance < k:

                for neighbor in self.adj_list[node]:

                    if neighbor not in visited:

                        visited.add(neighbor)

                        queue.append((neighbor, distance + 1))

        return result

    # =================================================
    # Bonus 4
    # Connected Components
    # =================================================
    def count_connected_components(self):

        visited = set()

        components = 0

        for vertex in self.adj_list:

            if vertex not in visited:

                components += 1

                queue = deque([vertex])

                visited.add(vertex)

                while queue:

                    current = queue.popleft()

                    for neighbor in self.adj_list[current]:

                        if neighbor not in visited:

                            visited.add(neighbor)

                            queue.append(neighbor)

        return components


# =====================================================
# PART A – BASIC GRAPH SETUP
# =====================================================

print("=" * 50)
print("PART A - BASIC GRAPH SETUP")
print("=" * 50)

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")

g.display()


# =====================================================
# PART B – BFS IMPLEMENTATION
# =====================================================

print("\n" + "=" * 50)
print("PART B - BFS IMPLEMENTATION")
print("=" * 50)

bfs_order = g.bfs("A")

print("\nBFS Traversal Order:")
print(" -> ".join(bfs_order))

"""
BFS Tree

        A
      /   \
     B     C
      \   /
        D
        |
        E
        |
        F

Visit Order:
A -> B -> C -> D -> E -> F
"""


# =====================================================
# PART C – DFS IMPLEMENTATION
# =====================================================

print("\n" + "=" * 50)
print("PART C - DFS IMPLEMENTATION")
print("=" * 50)

dfs_order = g.dfs("A")

print("\nDFS Traversal Order:")
print(" -> ".join(dfs_order))

"""
One Possible DFS Tree

A
|
B
|
D
|
C
|
E
|
F

Visit Order:
A -> B -> D -> C -> E -> F
"""

print("\nComparison Between BFS and DFS:")
print("""
BFS visits nodes level by level using a Queue.
It explores all neighboring vertices before moving deeper.

DFS visits nodes by going as deep as possible before backtracking.
It uses Recursion or a Stack.

Therefore BFS and DFS produce different traversal orders because
they follow different strategies for visiting vertices.
""")


# =====================================================
# PART D – BONUS / CHALLENGE TASKS
# =====================================================

print("\n" + "=" * 50)
print("PART D - BONUS TASKS")
print("=" * 50)

# Bonus 1 - Directed Graph

print("\nDirected Graph:")

directed_graph = Graph(directed=True)

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F")
]

for u, v in edges:
    directed_graph.add_edge(u, v)

directed_graph.display()

# Bonus 2 - Path Check

print("\nPath Checking:")

print("Path A -> F :", g.has_path("A", "F"))
print("Path B -> E :", g.has_path("B", "E"))
print("Path C -> F :", g.has_path("C", "F"))

# Bonus 3 - Social Network

print("\nPeople within 2 connections of A:")

print(g.within_k_connections("A", 2))

# Bonus 4 - Connected Components

print("\nNumber of Connected Components:")

print(g.count_connected_components())