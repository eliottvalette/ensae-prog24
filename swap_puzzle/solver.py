# This is the solver module. It contains the Solver class and its associated methods.
from grid import Grid
from graph import Graph
sequence_swaps=[] #global variable
class Solver(): 
    import os
    
    def __init__(self, m, n, initial_state):
        self.grid = Grid(m, n, initial_state)
        self.n = n
        self.m = m

    def find_coordinates_x(self, grid, x:int):
        """
        Get the cell's coordenates (i,j) of an integer

        Parameters: 
        -----------
        grid : Grid
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
    
    def drag_x(self, x:int):
        """
        Drag the integer x to it's correct place, without disturbing the precedent drags

        Parameters: 
        -----------
        x: int
            An integer from the grid.
        Output: 
        -------
        (i,j): tuple[int]
            The integer's cell coordenates.
        """
        (i, j) = self.find_coordinates_x(self.grid.state, x) # coordinates (i,j) of x in the non_sorted grid
        correct_matrix = Grid(self.m, self.n) # Without initial state in order to get a sorted matrix
        i_target, j_target = self.find_coordinates_x(correct_matrix.state, x)
        while j != j_target: # drag x to the correct column
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
        while i != i_target: # drag up x to the correct line, and thus the correct coordinate
            for k in range(i - i_target):
                sequence_swaps.append(((i, j), (i - 1, j)))
                self.grid.swap((i, j), (i - 1, j))
                i = i - 1

        current_state = Grid(self.m, self.n, self.grid.state) # update current state
        if current_state != correct_matrix:
            print(f"Current state after dragging {x}:")
            print(current_state)
    
    def get_solution(self):
        for x in range(1, self.m * self.n + 1):
            self.drag_x(x)
        return sequence_swaps
    
    @classmethod
    def get_solution_bfs(cls,graph:Graph):    
        with open ("tests/output_non_opti.txt","w") as f:
            for src in graph.nodes:
                for dst in graph.nodes:
                    if src < dst:
                        path = graph.bfs(src, dst)
                        if path:
                            distance = len(path) - 1
                            f.write(f"{src} {dst} {distance} {path}\n")
                        else:
                            f.write(f"{src} {dst} None\n")
    @classmethod
    def get_solution_bfs_opti(cls,graph:Graph):        
        with open ("tests/output_opti.txt","w") as f:
            for src in graph.nodes:
                for dst in graph.nodes:
                    if src < dst:
                        path = graph.bfs_opti(src, dst)
                        if path:
                            distance = len(path) - 1
                            f.write(f"{src} {dst} {distance} {path}\n")
                        else:
                            f.write(f"{src} {dst} None\n")
