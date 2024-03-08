from grid import Grid
from graph import Graph
from solver import Solver
import time 

print("\n\nTest des méthodes dans la classe Grid\n")
grid_file_name = "input/grid0.in"
grid = Grid.grid_from_file(grid_file_name)
dst_node = Grid(2, 2)

print("\nNodes :", grid.get_nodes())
print("\nCurrent state :", grid.state)
print("\nNeighbours of current state :", grid.get_neighbours())
current_state_key = grid.get_node_number(grid.state)
print(f"\n\nNeighbors of current state {current_state_key}: {list(grid.get_neighbours().keys())}")

print("\n\nConversion de la grille en graphe\n")
graph_from_grid = grid.generate_graph()
print("Graph:", graph_from_grid)

t1 = time.time()
graph_from_grid.get_solution_bfs()
t2 = time.time()
print("time non_opti :", t1-t2)

t3 = time.time()
graph_from_grid.get_solution_bfs_opti()
t4 = time.time()
print("time opti :", t3-t4)


#print(Solver.get_solution_bfs(graph_from_grid))