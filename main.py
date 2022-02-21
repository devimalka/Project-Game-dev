import pygame
from player import Player
from globalVars import *




pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Python Game Project")
#setting up fps
fps = pygame.time.Clock()

#loading image 
bg = pygame.image.load('assets/images/Hills Layer 01.png')
#scaling to screen width and height (pygame.transform.scale(image(width,height)))
bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

#player position Player(x,y)
player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
       


    point = pygame.mouse.get_pos()
    collide = player1.rect.collidepoint(point)
    print(collide)
    color = (255,56,100) if collide else (255,255,255)
    
    #loading screen with bg image
    screen.blit(bg,(0,0)) 
   

    player1.update()
    pygame.draw.rect(screen,color,player1.rect)  

    
    fps.tick(60)
    pygame.display.update()
