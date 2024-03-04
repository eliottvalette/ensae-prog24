from grid import Grid
from graph import Graph
from solver import Solver
import time 

print("\n\nTest de la méthode bfs dans la classe Graph")
graph_file_name = "input/graph2.in"
graph = Graph.graph_from_file(graph_file_name)
print("Graph:", graph)
src_node = 2
dst_node = 7
shortest_path = graph.bfs(src_node, dst_node)
print("Shortest path from node", src_node, "to node", dst_node, ":", shortest_path)

print("\n\nTest des méthodes dans la classe Grid")
grid_file_name = "input/grid0.in"
grid = Grid.grid_from_file(grid_file_name)
print(grid.state)
dst = Grid(2, 2).state
print(dst)
print("Grid:", grid)
print("All nodes of the grid:", grid.get_nodes())
print("Neighbors:", grid.get_neighbours())

print(grid.state)
print(Graph.bfs(grid.state,dst))
