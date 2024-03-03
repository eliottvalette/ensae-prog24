# This is the solver module. It contains the Solver class and its associated methods.
from grid import Grid
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
    
    @classmethod
    def get_solution_bfs(cls, g:Grid):
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
        return g.graph_from_grid().bfs(g.grid_as_tuple(),Grid(g.m,g.n).grid_as_tuple())
    
    @staticmethod
    def get_solution_BFS_op(grid):
        """
        Solves the grid using a specific BFS algorithm that visits only the necessary part of the graph.

        Parameters: 
        -----------
        grid: Grid
            The grid to solve

        Output: 
        -------
        path: list[tuple]
            The path of swaps leading to the sorting the intial grid.
        """

        Solution = Grid(grid.m, grid.n).grid_as_tuple()
        Queue = [grid.grid_as_tuple()]
        Visited = []
        Parent = dict()
        Found = False

        while Queue != [] and not(Found) :
            Current_grid = Queue.pop(0)
            if Current_grid not in Visited:
                Visited.append(Current_grid)
                
                # On crée une liste de liste à partir du tuple de tuple
                L = []
                for k in Current_grid:
                    L.append(list(k))
                
                Next_grids = Grid(len(L),len(L[0]),L).adjacent_grids()
                
                for (N,swap) in Next_grids:
                    if N not in Parent.keys():
                        Parent[N] = (Current_grid,swap)
                        Queue.append(N)
                    if N == Solution:
                        Found = True
        path = []
        N = Solution
        while N != grid.grid_as_tuple():
            N,swap = Parent[N]
            path.append(swap)
        path.reverse()
        return path
    


grid = Grid.grid_from_file("input/grid4.in")
solver = Solver(grid.m, grid.n, grid.state)
print(solver.get_solution())

