import pygame
class window:
    def __init__(self,height,width,title):       
        self.screen = pygame.display.set_mode((height,width))
        pygame.display.set_caption(title)
        icon = pygame.image.load('assets/icon.ico')
        pygame.display.set_icon(icon)    