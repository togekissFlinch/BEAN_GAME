import pygame
class object:
    def __init__(self,sprite,x,y):
        self.sprite = pygame.image.load("assets/" + sprite + ".png")
        self.x = x
        self.y = y
