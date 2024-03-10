
#main.py
from grid import Grid
from graph import Graph
from solver import Solver
import time 

# Initialisation des variables
grid_file_name = "input/grid1.in"
grid = Grid.grid_from_file(grid_file_name)
sorted_grid = Grid(grid.m,grid.n).state
current_state_key = grid.get_node_number(grid.state)
graph_from_grid = grid.generate_graph()

############
# Séance 1 #
############
print("\n\nTest de la méthode naïve")
solver = Solver(grid.m, grid.n, grid.state)
print("Swap sequence solution :", solver.get_solution())

##################
# Séance 2, 3, 4 #
##################

# Initialisation des variables
grid_file_name = "input/grid0.in"
grid = Grid.grid_from_file(grid_file_name)
sorted_grid = Grid(grid.m,grid.n).state
current_state_key = grid.get_node_number(grid.state)
graph_from_grid = grid.generate_graph()

# Impression des variables
print("\n\nSéance 2, 3 ,4")
print("\nImpression des variables :")
print("\nNodes :", grid.get_nodes())
print("\nCurrent state :", grid.state)
print("\nNeighbours of current state :", grid.get_neighbours())
print(f"\nNeighbors of current state {current_state_key}: {list(grid.get_neighbours().keys())}")

print("\nConversion de la grille en graphe")
print("Graph:", graph_from_grid)

print("Test des méthodes du bfs : l'output dans le dossier test")
Solver.get_solution_bfs(graph_from_grid)
Solver.get_solution_bfs_opti(graph_from_grid)

print("\nTest des méthodes de la methode A*")
print("\nShortest path using A* method: ", grid.optimized_solver_astar(grid,grid.m,grid.n))