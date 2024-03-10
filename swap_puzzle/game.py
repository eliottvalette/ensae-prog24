import pygame
import random as rd
from grid import Grid
from solver import Solver
import time
from itertools import permutations
import numpy as np

# Initialisation des variables
row,column = 3,4

# Initialisation de Pygame
clock = pygame.time.Clock()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Définition de la taille de la fenêtre
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
TILE_SIZE = 750/max(row,column)

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Puzzle Game")

# Trouver un grille aléatoire
def get_random_grid(row,column):
        numbers = range(1, row * column + 1)
        all_permutations = [list(line) for line in permutations(numbers)] # generate a list of lists, each list in a unique permutation of numbers
        list_matrix=[]
        for permutation in all_permutations:
            current_matrix=[]
            for i in range(row):
                current_matrix.append(permutation[column*i:column*(i+1)]) # According to the shape (m,n) transform each list in matrix
            list_matrix.append((current_matrix)) # list of unique shuffled matrix
        return rd.choice(list_matrix)

# Initialisation du Jeu
grid = Grid(row,column)
playing_grid = get_random_grid(row,column)

# Fonction pour afficher la grille
def draw_grid(grid):
    print('drawing...')
    m,n=np.shape(grid)
    print((m,n))
    for i in range(m):
        for j in range(n):
            pygame.draw.rect(window, WHITE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
            number = grid[i][j]
            if number != m * n:
                font = pygame.font.SysFont(None, 48)
                text = font.render(str(number), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE / 2, i * TILE_SIZE + TILE_SIZE / 2))
                window.blit(text, text_rect)
    pygame.display.update()

def main():
    # Boucle principale du jeu
    running = True
    draw_grid(playing_grid)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_tile_row = mouse_pos[1] // TILE_SIZE
                clicked_tile_col = mouse_pos[0] // TILE_SIZE
    clock.tick(30)
    pygame.display.update()

# Lancement du jeu
pygame.init()
running=True
while running:
    main()

pygame.quit()
