from tkinter import LEFT
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_UP, Rect
import pygame
#importing global variables
from globalVars import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #creating rect with position of x,y and width and height(Rect(x,y,width,height))
        self.rect = Rect(x, y, 150, 150)

    def update(self):
        px = 0
        py = 0

        #get key events
        key = pygame.key.get_pressed()

        if key[K_RIGHT]:
            px += 5
        elif key[K_LEFT]:
            px -= 5
        elif key[K_DOWN]:
            py += 5
        elif key[K_UP]:
            py -= 5


       
      
    

        #player rect position update
        self.rect.x += px
        self.rect.y += py
        
        # x axis collision |<-
        if self.rect.x <=0:
            self.rect.x = 0
        # y axis collision |<-    
        if self.rect.y <= 0:
            self.rect.y = 0
        

        print("self.rect.x = {}".format(self.rect.x))
        print("self.rect.y = {}".format(self.rect.y))
      

    

    
