from curses import KEY_DOWN
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 450



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Python Game Project")




while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            
    pygame.display.update()