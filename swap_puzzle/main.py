from grid import Grid
from graph import Graph
from solver import Solver
import time 


# g = Grid(4,4,[[16,14,3,10],[4,5,6,11],[7,15,8,12],[13,2,9,1]])

# t0 = time.time()
# print(Solver.get_solution(g))
# t1 = time.time()
# print(t1-t0)

print("\n\nTest de la méthode bfs dans la classe Graph")
graph_file_name = "input/graph1.in"
graph = Graph.graph_from_file(graph_file_name)
print("Graph:", graph)
src_node = 2
dst_node = 7
shortest_path = graph.bfs(src_node, dst_node)
print("Shortest path from node", src_node, "to node", dst_node, ":", shortest_path)

print("\n\nTest des méthodes dans la classe Grid")
grid_file_name = "input/grid0.in"
grid = Grid.grid_from_file(grid_file_name)
print("Grid:", grid)
print("All nodes of the grid:", grid.get_nodes())
