import pygame
class Bean: 
    def __init__(self):
        self.sprite = pygame.image.load('/Users/gang-guhyeon1/Desktop/Python/Flappuccino-main/data/gfx/bean.png')
        self.position = pygame.Vector2()
        self.position.xy