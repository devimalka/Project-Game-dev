from pygame import Rect


class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = Rect(0,0,50,50)


    def update(self):
        self.rect.x += 5
        self.rect.y += 1

    

    