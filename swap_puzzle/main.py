from grid import Grid
from solver import Solver
import time 


g = Grid(4,4,[[16,14,3,10],[4,5,6,11],[7,15,8,12],[13,2,9,1]])
#On vérifie que la fenêtre graphique s'affiche bien

#g.graphique()

t0 = time.time()
print(Solver.get_solution(g))
t1 = time.time()
print(t1-t0)
#print(Solver.get_solution_BFS_op(g))
t2 = time.time()
print(t2-t1)
print(Solver.get_solution_A_star(g))
t3 = time.time()
print(t3-t2)

g = Grid.grid_from_file("input/grid3.in")
print(Solver.get_solution_A_star(g))
print(Solver.get_solution_BFS_op(g))

