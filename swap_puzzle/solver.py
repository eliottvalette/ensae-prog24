from grid import Grid

class Solver(): 
    
    def get_solution(self, grid):
        swaps_sequence = []
        for i in range(grid.m):
            for j in range(grid.n):
                for i_swap in range(i, grid.m):
                    start_j = j if i_swap == i else 0
                    for j_swap in range(start_j, grid.n):
                        if grid.state[i_swap][j_swap] == i_swap * grid.n + j_swap + 1:
                            continue  # Cellule déjà à la bonne position
                            
                        swaps_sequence.append(((i, j), (i_swap, j_swap)))
                        grid.swap((i, j), (i_swap, j_swap))
                        
        return swaps_sequence

                        




