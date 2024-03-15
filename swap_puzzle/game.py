""""
A game where the goal is to order the grid. To perform a swap, click the mouse on a tile and drag the number
to an adjacent tile.

"""

import pygame
import random
from grid import Grid
from graph import Graph
from solver import Solver

# Initialize Pygame
pygame.init()

# Initialize variables
lignes,colonnes = 2 , 2
not_too_big = ((lignes+colonnes)<7)

WINDOW_SIZE = (1200, 750)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Grid Swap Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (200,214,191)
CREAM=(249,249,200)
LIGHT_CREAM=(249,249,230)

GRID_SIZE = (lignes,colonnes) 

TILE_SIZE = min(WINDOW_SIZE[0] // GRID_SIZE[1], WINDOW_SIZE[1] // GRID_SIZE[0]) # Define tile size to properly fill our window with tiles

# Initialize the grid with random numbers between 1 and n*m
numbers = list(range(1, GRID_SIZE[0] * GRID_SIZE[1] + 1))
random.shuffle(numbers)
grid = Grid(lignes,colonnes,[numbers[i * GRID_SIZE[1]:(i + 1) * GRID_SIZE[1]] for i in range(GRID_SIZE[0])])

if not_too_big:
    solution = grid.optimized_solver_astar(grid,grid.m,grid.n)
    print("\nShortest path using A* method: ",solution)
    len_solution = len(solution)- 1

# Run the game loop
running = True
selected_tile = None
swap_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Record the tile clicked
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // TILE_SIZE, pos[0] // TILE_SIZE
            if 0 <= row < GRID_SIZE[0] and 0 <= col < GRID_SIZE[1]:
                selected_tile = (row, col)
                rect = pygame.Rect(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, CREAM, rect, 1)
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_tile:
                # Performe the swap
                row, col = event.pos[1] // TILE_SIZE, event.pos[0] // TILE_SIZE
                if (0 <= row < GRID_SIZE[0] and 0 <= col < GRID_SIZE[1] and
                    (abs(row - selected_tile[0]) + abs(col - selected_tile[1]) == 1)):
                    grid.state[row][col], grid.state[selected_tile[0]][selected_tile[1]] = (
                        grid.state[selected_tile[0]][selected_tile[1]], grid.state[row][col])
                    swap_count += 1 # Count each swap
                selected_tile = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset the grid with a new random arrangement of numbers
                numbers = list(range(1, GRID_SIZE[0] * GRID_SIZE[1] + 1))
                random.shuffle(numbers)
                grid = Grid(lignes,colonnes,[numbers[i * GRID_SIZE[1]:(i + 1) * GRID_SIZE[1]] for i in range(GRID_SIZE[0])])
                swap_count = 0  # Reset the swap count
                if not_too_big:
                    solution = grid.optimized_solver_astar(grid,grid.m,grid.n)
                    print("\nShortest path using A* method: ",solution)
                    len_solution = len(solution)- 1
            elif event.key == pygame.K_t:
                grid = Grid(lignes,colonnes,[numbers[i * GRID_SIZE[1]:(i + 1) * GRID_SIZE[1]] for i in range(GRID_SIZE[0])])# same grid
                swap_count = 0 # Reset the swap count


    # Draw the grid
    screen.fill(LIGHT_CREAM)
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if selected_tile and (i, j) == selected_tile:
                pygame.draw.rect(screen, CREAM, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
            value = grid.state[i][j]
            text = pygame.font.Font(None, int(TILE_SIZE * 0.6)).render(str(value), True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
    
    # Check if the grid is sorted in ascending order
    sorted_grid = [item for row in grid.state for item in row]
    if sorted_grid == list(range(1, GRID_SIZE[0] * GRID_SIZE[1] + 1)):
        screen.fill(GREEN)
        # Display congratulations message with the number of swaps made
        congrats_font = pygame.font.Font(None, 36)
        if not_too_big :
            congrats_bfs_text = congrats_font.render(f"Congratulations! You beat the game in {swap_count} swaps!", True, BLACK)
            however_text =congrats_font.render(f"However it could have been beaten in {len_solution} swaps...", True, BLACK)
            congrats_bfs_rect = congrats_bfs_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
            however_rect = congrats_bfs_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 2*36))
            screen.blit(congrats_bfs_text, congrats_bfs_rect)
            screen.blit(however_text, however_rect)
            pygame.display.flip()
        else :
            congrats_text = congrats_font.render(f"Congratulations! You beat the game in {swap_count} swaps!", True, BLACK)
            congrats_rect = congrats_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
            screen.blit(congrats_text, congrats_rect)
            pygame.display.flip()
     
    pygame.display.flip()
pygame.quit()