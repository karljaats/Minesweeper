import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            
    pygame.display.flip()
