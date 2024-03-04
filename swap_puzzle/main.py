from grid import Grid
from graph import Graph
from solver import Solver
import time 

# print("\n\nTest de la méthode bfs dans la classe Graph\n")
# graph_file_name = "input/graph1.in"
# graph = Graph.graph_from_file(graph_file_name)
# print("Graph:", graph)
# src_node = 2
# dst_node = 7
# shortest_path = graph.bfs(src_node, dst_node)
# print("Shortest path from node", src_node, "to node", dst_node, ":", shortest_path)

print("\n\nTest des méthodes dans la classe Grid\n")
grid_file_name = "input/grid0.in"
grid = Grid.grid_from_file(grid_file_name)
dst_node = Grid(2, 2)
print(grid)
print("All nodes of the grid:", grid.get_nodes())

neighbors = grid.get_neighbours()
current_state_key = grid.get_node_number(grid.state)
print(f"\n\nNeighbors of current state {current_state_key}: {list(neighbors.keys())}")

print("\n\nConversion de la grille en graphe\n")
graph_from_grid = grid.generate_graph()
print("Graph:", graph_from_grid)
shortest_path_grid = graph_from_grid.bfs(current_state_key, 1)
print("Shortest path from node", current_state_key, "to node", 1, ":", shortest_path_grid)

