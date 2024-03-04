# This is the solver module. It contains the Solver class and its associated methods.
from grid import Grid

sequence_swaps=[] #global variable
class Solver(): 
    def __init__(self, m, n, initial_state):
        self.grid = Grid(m, n, initial_state)
        self.n = n
        self.m = m

    def find_coordinates_x(self, grid, x:int):
        """
        Get the cell's coordenates (i,j) of an integer

        Parameters: 
        -----------
        grid
            The grid.
        x: int
            An integer from the grid.

        Output: 
        -------
        (i,j): tuple[int]
            The integer's cell coordenates.
        """
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == x: 
                    return (i, j)
    
    def drag_x(self, x):
        (i, j) = self.find_coordinates_x(self.grid.state, x) # (i,j) coordonnée de x dans la matrice non ordonnée
        correct_matrix = Grid(self.m, self.n) # Without initial state in order to get a sorted matrix
        i_target, j_target = self.find_coordinates_x(correct_matrix.state, x)
        while j != j_target: # On se place dans la meme colonne que la place objectif
            if j_target < j:
                for k in range(j - j_target):
                    sequence_swaps.append(((i, j), (i, j - 1)))
                    self.grid.swap((i, j), (i, j - 1))
                    j = j - 1
            else:
                for k in range(j_target - j):
                    sequence_swaps.append(((i, j), (i, j + 1)))
                    self.grid.swap((i, j), (i, j + 1))
                    j = j + 1
        while i != i_target: # On remonte dorit vers l'objectif pour ne pas déranger ce qui a été fait
            for k in range(i - i_target):
                sequence_swaps.append(((i, j), (i - 1, j)))
                self.grid.swap((i, j), (i - 1, j))
                i = i - 1

        current_state = Grid(self.m, self.n, self.grid.state)
        if current_state != correct_matrix:
            print(f"Current state after dragging {x}:")
            print(current_state)
    
    def get_solution(self):
        for x in range(1, self.m * self.n + 1):
            self.drag_x(x)
        return sequence_swaps
    
    def get_solution_bfs(self, grid:Grid):
        """
        Solves the grid using the BFS algorithm.

        Parameters: 
        -----------
        g: Grid
            The grid to solve.

        Output: 
        -------
        list[tuple]
            The list of the differents grid's states leading to its solved state.
        """
        return grid.graph_from_grid().bfs(grid.grid_as_tuple(),Grid(grid.m,grid.n).grid_as_tuple())
    

# grid = Grid.grid_from_file("input/grid4.in")
# solver = Solver(grid.m, grid.n, grid.state)
# print(solver.get_solution())

