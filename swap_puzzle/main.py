from grid import Grid
from graph import Graph

g = Grid(2, 3)
print(g)

data_path = "input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
print(f"\n {g.get_all_nodes(g.m,g.n)} \n")


graph_file_name = data_path + "graph1.in"
graph = Graph.graph_from_file(graph_file_name)

print(f"\n {graph} \n")

src = 2
dst = 7
shortest_path = graph.bfs(src, dst)

print(f"{src} {dst} {len(shortest_path)-1} {shortest_path}")
