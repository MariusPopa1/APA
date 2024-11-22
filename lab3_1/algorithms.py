from collections import defaultdict, deque


class GraphDFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)


class GraphBFS:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    def show(self, adjList):
        for key, value in adjList.items():
            print(key, "   ", value, "\n")
    def bfs(self, startNode):
        queue = deque()
        max_node = max(self.adjList.keys(), default=-1)
        visited = [False] * (max_node + 1)

        visited[startNode] = True
        queue.append(startNode)

        while queue:

            currentNode = queue.popleft()

            for neighbor in self.adjList[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)