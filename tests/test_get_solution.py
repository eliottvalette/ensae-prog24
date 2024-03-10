import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

grid_file_name = "input/grid1.in"

class Test_GetSolution(unittest.TestCase):
    def test_sorted_grid(self):
        grid = Grid.grid_from_file(grid_file_name)
        grid.state=[[1, 2], [3, 4], [5, 6], [7, 8]]
        print(grid.state)
        solver = Solver(grid.m, grid.n, [[1, 2], [3, 4], [5, 6], [7, 8]])
        solution = solver.get_solution()
        self.assertEqual(solution, [])

    def test_partially_sorted_grid(self): 
        grid = Grid.grid_from_file(grid_file_name)
        grid.state=[[1, 2], [3, 4], [5, 6], [8, 7]]
        solver = Solver(grid.m, grid.n, grid.state)
        solution = solver.get_solution()
        # Dans ce cas, seul un swap est nécessaire pour trier la grille.
        self.assertEqual(solution, [((3, 1), (3, 0))])

    def test_unsorted_grid(self):
        grid = Grid.grid_from_file(grid_file_name)
        grid.state=[[2, 1], [4, 3], [5, 6], [8, 7]]
        solver = Solver(grid.m, grid.n, grid.state)
        solution = solver.get_solution()
        # Dans ce cas, plus d'un swap est nécessaire pour trier la grille.
        self.assertTrue(len(solution) > 1)

if __name__ == '__main__':
    unittest.main()