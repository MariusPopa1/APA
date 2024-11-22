from collections import defaultdict
# Class to represent a graph using adjacency list


class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def dsf_util(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dsf_util(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def dfs(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.dsf_util(v, visited)


# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")

    # Function call
    g.dfs(2)
