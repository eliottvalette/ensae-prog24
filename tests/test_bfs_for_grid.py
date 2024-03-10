import sys 
sys.path.append("swap_puzzle/")


import unittest
from graph import Graph
from grid import Grid
from solver import Solver

class Test_BFS(unittest.TestCase):
    def test_graph1(self):
        grid_file_name = "input/grid0.in"
        grid = Grid.grid_from_file(grid_file_name)
        graph_from_grid = grid.generate_graph()
        Solver.get_solution_bfs(graph_from_grid)
        with open("tests/bfs.txt", "r") as file:
            resultat_observe = file.read()

        with open("tests/grid1_verified_output.txt", "r") as file:
            resultat_attendu = file.read()
        
        self.assertEqual(resultat_observe, resultat_attendu)
if __name__ == '__main__':
    unittest.main()
