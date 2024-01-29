from grid import Grid
import numpy as np

class Solver(): 
    def __init__(self , m , n ,initial_state):
        self_grid = Grid(m,n,initial_state)
        self.n = self_grid.n
        self.m = self_grid.m
        self.state = self_grid.state

    def find_coordinates_x(self, grid, x):
        for i in range(self.m):
            for j in range(self.n):
                if grid.state[i][j] == x:
                    return (i,j)
    
    def drag_x(self, x):
        (i,j) = self.find_coordinates_x(self.state, x)
        correct_matrix = Grid(self.m,self.n)
        i_target,j_target = self.find_coordinates_x(correct_matrix , x)
        while j!=j_target:
            if j_target<j:
                for k in range(j-j_target):
                    self.swap((i,j),(i,j-1))
                    j=j-1
            else:
                for k in range(j_target-j):
                    self.swap((i,j),(i,j+1))
                    j=j+1
        while i!=i_target:
            for k in range(i-i_target):
                self.swap((i,j),(i-1,j))
                i=i-1
    
    def get_solution(self):
        for x in range(self.m*self.n):
            self.drag_x(x+1)

        

                        




