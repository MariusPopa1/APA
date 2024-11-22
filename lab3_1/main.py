import time
import matplotlib.pyplot as plt
from lab3_1.algorithms import *
import pandas as pd
from networkx.generators.random_graphs import erdos_renyi_graph

values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
timeDFS = []
timeBFS = []


for i in values:
    g = erdos_renyi_graph(i, 0.95)
    graph = GraphDFS()
    for a in g.edges:
        n, e = a
        graph.addEdge(n, e)
    start = time.perf_counter()
    graph.DFS(0)
    end = time.perf_counter()
    timeDFS.append(end - start)

for i in values:
    g = erdos_renyi_graph(i, 0.95)
    graph = GraphBFS()
    for a in g.edges:
        n, e = a
        graph.addEdge(n, e)
    start = time.perf_counter()
    graph.bfs(0)
    end = time.perf_counter()
    timeBFS.append(end - start)  

plt.plot(values, timeDFS, label="Depth First Search")
plt.plot(values, timeBFS, label="Breadth First Search")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Graph Traversal Algorithms')
plt.legend()  # Adding legend
plt.show()

data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timeDFS[i], timeBFS[i]])

# Display results in a tables
headers = ["Input Size", 'DFS', 'BFS']
df = pd.DataFrame(data, columns=headers)
print(df)
