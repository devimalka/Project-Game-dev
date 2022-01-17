from tkinter import LEFT
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_UP, Rect
import pygame
import pygments


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(0, 0, 50, 50)

    def update(self):
        px = 0
        py = 0
        key = pygame.key.get_pressed()

        if key[K_RIGHT]:
            px += 5
        elif key[K_LEFT]:
            px -= 5
        elif key[K_DOWN]:
            py += 5
        elif key[K_UP]:
            py -= 5
      
    


        self.rect.x += px
        self.rect.y += py
       

    

    
