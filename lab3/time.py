import timeit as t
from main import Graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.dfs(0)
