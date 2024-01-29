# This will work if ran from the root folder ensae-prog24
import sys
sys.path.append("swap_puzzle/")

import unittest
from grid import Grid
from solver import Solver

class Test_GetSolution(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        solver = Solver()
        solution = solver.get_solution(grid)
        grid.swap_seq(solution)
        self.assertEqual(grid.is_sorted(), True)

if __name__ == '__main__':
    unittest.main()
