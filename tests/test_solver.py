# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")
# Importez la classe Grid et la classe Solver
from grid import Grid
from solver import Solver  # Assurez-vous que le nom du fichier est correct

# Créez une instance de la classe Grid à partir d'un fichier d'entrée
grid = Grid.grid_from_file("input/grid1.in")

# Créez une instance de la classe Solver
solver = Solver()

# Appelez la méthode get_solution avec la grille en tant qu'argument
solution = solver.get_solution(grid)

# Affichez la solution
print("Solution obtenue:", solution)