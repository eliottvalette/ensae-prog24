import sys 
sys.path.append("swap_puzzle/")


import unittest
from grid import Grid

class TestAStar(unittest.TestCase):
    def test_a_star_solution(self):
        # Define an initial grid
        grid_file_name = "input/grid0.in"
        grid = Grid.grid_from_file(grid_file_name)
        
        # Get the solution using A*
        solution = grid.optimized_solver_astar(grid,grid.m,grid.n)
        
        # Define the expected solution
        expected_solution = [
            (2, 4, 3, 1), 
            (2, 1, 3, 4), 
            (1, 2, 3, 4)
        ]
        
        # Check if the generated solution matches the expected solution
        self.assertEqual(solution, expected_solution)

if __name__ == '__main__':
    unittest.main()
