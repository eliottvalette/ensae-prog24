"""
This is the main module.
"""
from grid import Grid
from graph import Graph
from solver import Solver
import time 

print("\n\nTest de la méthode bfs dans la classe Graph\n")
graph_file_name = "input/graph2.in"
graph = Graph.graph_from_file(graph_file_name)
print("Graph:", graph)
src_node = 2
dst_node = 7
shortest_path = graph.bfs(src_node, dst_node)
print("Shortest path from node", src_node, "to node", dst_node, ":", shortest_path)

print("\n\nTest des méthodes dans la classe Grid\n")
grid_file_name = "input/grid4.in"
grid = Grid.grid_from_file(grid_file_name)
print(grid.state)
dst_node = Grid(2, 2).grid_as_tuple()
print(dst_node)
print("Grid:", grid)
print("All nodes of the grid:", grid.get_nodes())
print("\n\nNeighbors:", grid.get_neighbours())
