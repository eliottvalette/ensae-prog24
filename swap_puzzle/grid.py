"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import numpy as np
import copy
from itertools import permutations
from graph import Graph
import heapq

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = "The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
        """
        return (self.state==Grid(self.m,self.n).state)


    def is_swap_valid(self, i1, j1, i2, j2):
        """
        Parameters: 
        -----------
        i1, j1, i2, j2: int

        Checks is the swap valid using the formula in the statement
        """
        return (i1==i2 and abs(j1-j2)==1) or (abs(i1-i2)==1 and j1==j2)
    
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell.
        """
        i1, j1 = cell1
        i2, j2 = cell2
        
        # Verification that swap is allowed
        if self.is_swap_valid(i1, j1, i2, j2):
            # Simultaneous inversion
            self.state[i1][j1], self.state[i2][j2] = self.state[i2][j2], self.state[i1][j1]
        else :    
            raise ValueError("Invalid swap")
     
    def generate_swaped(self, grid, cell1, cell2):
        """
        Implements the swap operation between two cells. 
        But returning the swaped grid, without affecting the self grid.

        Parameters: 
        -----------
        grid : Grid.state

        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell.

        """
        i1, j1 = cell1
        i2, j2 = cell2

        grid_copy=copy.copy(grid)
        
        # Verification that swap is allowed
        if self.is_swap_valid(i1, j1, i2, j2) :
            # Simultaneous inversion
            grid_copy[i1][j1], grid_copy[i2][j2] = grid_copy[i2][j2], grid_copy[i1][j1]
            return grid_copy
        else :    
            raise ValueError("Invalid swap")

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for swap_pair in cell_pair_list:
            self.swap(swap_pair[0], swap_pair[1])
    
    def get_nodes(self):
        """
        According to the shape of self, returns a dict whose keys or intergers from 1 to fact(m*n).
        Each integer is liked to a value, a unique state of a grid (m,n)
        NB : The value of key 1 is the sorted grid .
        """
        m,n = self.m,self.n
        numbers = range(1, m * n + 1)
        all_permutations = [list(row) for row in permutations(numbers)] # generate a list of lists, each list in a unique permutation of numbers
        list_matrix=[]
        for permutation in all_permutations:
            current_matrix=[]
            for i in range(m):
                current_matrix.append(permutation[n*i:n*(i+1)]) # According to the shape (m,n) transform each list in matrix
            list_matrix.append((current_matrix)) # list of unique shuffled matrix
        dict_nodes={}
        for k in range(len(list_matrix)): # Associate each matrix to an integer
            dict_nodes[k+1]=list_matrix[k]
        return dict_nodes 
    
    def are_neighbours(self,initial,friend):
        """
        Calling generate_swaped, verifies if, by doing only one swap, initial and friend can be equal. 
        If so, initial and friend are neighbours
        
        Parameters: 
        -----------
        initial, friend: grid.state

        Returns boolean
        """
        for i in range(self.m): # explore all horizontal swaps
            for j in range(self.n-1):
                if initial==self.generate_swaped(friend,(i,j),(i,j+1)):
                    return True
          
        for i in range(self.m-1):# explore all vertical swaps
            for j in range(self.n):
                if initial==self.generate_swaped(friend, (i,j),(i+1,j)):
                    return True
        return False # Inital and Friend are equal or separated by more than one swap
    
    def get_neighbours(self):
        """
        Returns a dict containing only the neigbours' keys and values of self
        """
        nodes = self.get_nodes()
        current_permutation = self.state
        neighbours = {}
        for node_key, node_permutation in nodes.items(): # (int, grid.state)
            node_copy = copy.copy(node_permutation) # prevent modifying node_permutation
            if node_permutation !=(current_permutation) and self.are_neighbours(current_permutation, node_copy):
                neighbours[node_key] = node_permutation
        return neighbours
    
    def get_node_number(self, state):
        """
        Get the node number corresponding to the given position in the grid.

        Parameters:
        -----------
            position : Grid.state
                The key associated to state in the dict of self nodes

        Output:
        -----------
            int: The node number corresponding to the given key.
        """
        for node_number, node_position in self.get_nodes().items():
            if node_position == state:
                return node_number
        raise ValueError("Node position not found in the grid.")
    
    def generate_graph(self):
        """
        Generate a graph from the grid.

        Returns:
        --------
        Graph: The graph representing the grid.
        """
        nodes=list(self.get_nodes().keys())
        graph = Graph(nodes) # graph with m*n nodes but no edges

        for node_key, node_permutation in self.get_nodes().items():
            valid_neighbours = []
            for neighbor_key, neighbor_permutation in self.get_nodes().items(): # Add neigbours to a list of neighbours
                if self.are_neighbours(node_permutation, neighbor_permutation):
                    valid_neighbours.append(neighbor_key)

            for neighbor_key in valid_neighbours: # Add edges between node and neighbours
                if (neighbor_key,node_key) not in graph.edges: # Prevent duplicates of edges (a,b) and (b,a)
                    graph.add_edge(node_key, neighbor_key)
        return graph

    @staticmethod
    def from_grid_to_tuple(grid):
        """
        Parameters:
        -----------
            grid : Grid

        Returns tuple(int)
        """
        tupled_grid = []
        for line in grid: # explicit
            for coef in line:
                tupled_grid.append(coef)
        return tuple(tupled_grid)
    
    @staticmethod
    def from_grid_to_tuple_of_tuple(grid):
        """
        Parameters:
        -----------
            grid : Grid

        Returns tuple(tuple(int))
        """
        tupled_grid = []
        for line in grid: # explicit
            tupled_grid = tuple(line)
        return tupled_grid
    
    @staticmethod
    def from_tuple_to_matrix(tuple, m, n):
        """
        Parameters:
        -----------
            tuple : tuple
                tuple of it representing the permutation of the target matrix

            m,n = int
                shape of the target matrix

        Returns list(list(int))
        """
        matrix = []
        for i in range(m):
            matrix.append(list(tuple[i * n:(i + 1) * n]))
        return list(matrix)

    def manhattan_distance(self, node):
            """
            Calculates the Manhattan distance between two grid states.

            Parameters:
            -----------
            node: grid
                Grid states to compare.

            Returns:
            --------
            int:
                Manhattan distance between the two grid states.
            """

            def find_coordinates_x(grid, x:int):
                """
                Get the cell's coordenates (i,j) of an integer

                Parameters: 
                -----------
                grid : grid.state
                    The state of grid
                x: int
                    An integer from the grid.

                Output: 
                -------
                (i,j): tuple[int]
                    The integer's cell coordenates.
                """
                for i in range(self.m): # explicit
                    for j in range(self.n):
                        if grid[i][j] == x: 
                            return (i, j)
                        
            sorted_grid = Grid(self.m, self.n) # Without initial state in order to get a sorted matrix
            node = Grid.from_grid_to_tuple(node)

            distance = 0
            for k in node :
                i1, j1 = find_coordinates_x(sorted_grid.state,k)
                i2, j2 = find_coordinates_x(self.state,k)
                distance += abs(i1 - i2) + abs(j1 - j2) # definition of manhattan distance

            return distance
        
    def a_star(self, start_grid, m, n):
        """
        Implements the A* algorithm to find the shortest path from an initial grid to a sorted grid.

        Parameters:
        -----------
        start_grid: grid
            initial grid
        m: int
            Number of grid lines.
        n: int
            Number of grid columns.

        Returns:
        --------
        path: list[tuple[int]] | None
            Shortest path from initial state to final state. Returns None if the path is not found.
        """
        start = Grid.from_grid_to_tuple(start_grid)
        goal = Grid.from_grid_to_tuple(Grid(m, n).state)

        priority_queue = [(0, start, [])]  # (priority, node, path)
        visited = set()

        while priority_queue:
            current_cost, current_node, current_path = heapq.heappop(priority_queue)

            if current_node == goal: # If the current node is the goal state, return the path
                return current_path + [current_node]

            if current_node not in visited: # Avoid visiting the same node twice
                visited.add(current_node)
                current_node_matrix = Grid.from_tuple_to_matrix(current_node, m, n)
                current_neighbours_dict = Grid(m, n, current_node_matrix).get_neighbours()

                for neighbor_key in current_neighbours_dict.keys():
                    neighbor_state = Grid.from_grid_to_tuple(current_neighbours_dict[neighbor_key])
                    new_cost = current_cost + 1 # Cost of reaching the neighbor from the current node
                    heuristic_value = self.manhattan_distance(current_neighbours_dict[neighbor_key])
                    priority = new_cost + heuristic_value # Total priority for the neighbor
                    heapq.heappush(priority_queue, (priority, neighbor_state, current_path + [current_node]))

        return None #The goal isn't reached

    def optimized_solver_astar(self, grid, m, n):
            """
            Uses the A* algorithm to find the shortest solution to the grid problem.

            Parameters:
            -----------
            grid: Grid
                The instance of the Grid class representing the puzzle grid.
            
            m: int
                Number of grid lines.
            n: int
                Number of grid columns.

            Returns:
            --------
            path: list[tuple[int]] | None
                The shortest path from the initial state to the final state.
            """
            path = self.a_star(grid.state,m,n)
            return path
    
    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid