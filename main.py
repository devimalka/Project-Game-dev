import pygame
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Python Game Project")

bg = pygame.image.load('assets/images/Hills Layer 01.png')

player1 = Player(45,8)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
       


    screen.blit(bg,(0,0))   
    player1.update()

    pygame.draw.rect(screen,(255,0,0),player1.rect)
    pygame.display.update()
