"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import numpy as np
import copy
from itertools import permutations
from graph import Graph

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
        return (self.state==[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)])


    # faire isswapvalid
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell.

        Lets remain in line with the notations on page 3 
        """
        i1, j1 = cell1
        i2, j2 = cell2
        
        # Verification that swap is allowed
        if (i1==i2 and abs(j1-j2)==1) or (abs(i1-i2)==1 and j1==j2) :
            # Simultaneous inversion
            self.state[i1][j1], self.state[i2][j2] = self.state[i2][j2], self.state[i1][j1]
        else :    
            raise ValueError("Invalid swap")
        
    def swap_2(self, grid, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell.

        Lets remain in line with the notations on page 3 
        """
        i1, j1 = cell1
        i2, j2 = cell2

        grid_copy=copy.deepcopy(grid)
        
        # Verification that swap is allowed
        if (i1==i2 and abs(j1-j2)==1) or (abs(i1-i2)==1 and j1==j2) :
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
        m,n = self.m,self.n

        numbers = range(1, m * n + 1)
        all_permutations = [list(row) for row in permutations(numbers)]
        list_matrix=[]
        for permutation in all_permutations:
            current_matrix=list()
            for i in range(m):
                current_matrix.append(permutation[n*i:n*(i+1)])
            list_matrix.append((current_matrix))
        dict_nodes={}
        for k in range(len(list_matrix)):
            dict_nodes[k+1]=list_matrix[k]
        return dict_nodes
    
    def are_neighbours(self,initial,friend):
        for i in range(self.m):
            for j in range(self.n-1):
                if initial==self.swap_2(friend,(i,j),(i,j+1)):
                    return True
          
        for i in range(self.m-1):
            for j in range(self.n):
                if initial==self.swap_2(friend, (i,j),(i+1,j)):
                    return True
        return False
    
    def get_neighbours(self):
        nodes = self.get_nodes()
        current_permutation = self.state
        print("current_permutation : ")
        print(current_permutation)
        neighbours = []

        for node_key, node_permutation in nodes.items():
            node_copy = copy.deepcopy(node_permutation)
            if node_permutation !=(current_permutation) and self.are_neighbours(current_permutation, node_copy):
                neighbours.append(node_permutation)

        return neighbours
    
    def get_node_number(self, position):
        """
        Get the node number corresponding to the given position in the grid.

        Parameters:
        -----------
            position (tuple): The position of the node in the grid, represented as a tuple of tuples.

        Output:
        -----------
            int: The node number corresponding to the given position.
        """
        for node_number, node_position in self.get_nodes().items():
            if node_position == position:
                return node_number
        raise ValueError("Node position not found in the grid.")
    
    def permu(self,n):
        """
        Generate all the possible permutations from 1 to n

        Parameters: 
        -----------
        n: int
            Length of the list.

        Output: 
        -------
        perm: list[list]
            The list of all the permutations of the initial list.
        """
        L = list(range(1,n+1))
        permutations = list(permutations(L))
        return permutations

    def grid_as_tuple(self):
        """
        Renvoie l'état d'une grille sous la forme d'un tuple
        """
        T = []
        for k in range(len(self.state)):
            T.append(tuple(self.state[k]))
        T = tuple(T)
        return T
    
    def copy(self):
        """
        Retourne une copie d'une grille, liée à une liste indépendante
        """
        return Grid(self.m,self.n,copy.deepcopy(self.state))

    def all_state_grid(self):
        """
        Renvoie tous les états de la grilles possibles comme une liste de noeuds
        (tuples de tuples qui correspondent à toutes les grilles possibles)
        """
        nodes = []
        n=self.n*self.m
        L = Grid.permu(n)
        for i in L :
            node = []
            grid = list(i)
            for k in range(self.m):
                node.append(grid[self.n*k:(k+1)*self.n])
            # Converts the node from a list of lists to a tuple of tuples
            for k in range(len(node)):
                node[k] = tuple(node[k])
            node = tuple(node)
            nodes.append(node)
        print("nodes : " + str(nodes))
        return nodes
    
    def graph_from_grid(self):
        """
        Renvoie le graphe à partir d'une grille,
        c'est-à-dire tous les états de la grilles possibles (sous forme de tuples de tuples)
        avec toutes les liaisons posssibles correspondant aux swaps possibles
        """
        nodes = self.all_state_grid()
        graph_grid = Graph(nodes)
        for grid_tuple in nodes :

            # On convertit le tuple en liste
            grid_list = []
            for i in range(len(grid_tuple)):
                for j in range(len(grid_tuple[i])):
                    grid_list[i].append(grid_tuple[i][j])

            # On crée la grille à partir de la liste
            grid = Grid(len(grid_list[1]),len(grid_list[0]),grid_list)

            # On fait tous les swaps horizontaux et on ajoute les edges
            for i in range(grid.n-1):
                for j in range(grid.m):
                    grid2 = grid.copy()
                    grid2.swap((j,i),(j,i+1))
                    graph_grid.add_edge(grid.grid_as_tuple(),grid2.grid_as_tuple())

            # On fait tous les swaps verticaux on ajoute les edges
            for i in range(grid.m-1):
                for j in range(grid.n):
                    grid2 = grid.copy()
                    grid2.swap((i,j),(i+1,j))
                    graph_grid.add_edge(grid.grid_as_tuple(),grid2.grid_as_tuple())

        return graph_grid

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
    
    def adjacent_grids(self):
        
        """
        Generate all possible grids resulting from a swap operated on the initial grid

        Parameters: 
        -----------
        grid: Grid
            The initial grid

        Output: 
        -------
        grid_lst: list[tuple]
            The list of all possible grids (as tuple of tuples) resulting from a swap operated on the initial grid and the corresponding swap
        """

        grid_lst = []

        # On fait tous les swaps horizontaux et on ajoute les edges
        for i in range(self.n-1):
            for j in range(self.m):
                other = self.copy()
                other.swap((j,i),(j,i+1))
                grid_lst.append((other.grid_as_tuple(),((j,i),(j,i+1))))

        # On fait tous les swaps verticaux on ajoute les edges
        for i in range(self.m-1):
            for j in range(self.n):
                other = self.copy()
                other.swap((i,j),(i+1,j))
                grid_lst.append((other.grid_as_tuple(),((i,j),(i+1,j))))
        
        return grid_lst