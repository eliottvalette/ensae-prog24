from grid import Grid
from graph import Graph
from solver import Solver
import time 


g = Grid(4,4,[[16,14,3,10],[4,5,6,11],[7,15,8,12],[13,2,9,1]])

t0 = time.time()
print(Solver.get_solution(g))
t1 = time.time()
print(t1-t0)


g = Grid(2, 3)
print(g)

data_path = "input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


graph_file_name = data_path + "graph1.in"
graph = Graph.graph_from_file(graph_file_name)

print(graph.bfs)
print(graph)
