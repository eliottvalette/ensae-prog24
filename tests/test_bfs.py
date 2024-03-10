import sys 
sys.path.append("swap_puzzle/")


import unittest
from graph import Graph
from solver import Solver

class Test_BFS(unittest.TestCase):
    def test_graph1(self):
        graph = Graph.graph_from_file("input/graph1.in")
        Solver.get_solution_bfs(graph)
        with open("tests/bfs.txt", "r") as file:
            resultat_observe = file.read()

        with open("input/graph1.path.out", "r") as file:
            resultat_attendu = file.read()
        
        self.assertEqual(resultat_observe, resultat_attendu)
if __name__ == '__main__':
    unittest.main()
