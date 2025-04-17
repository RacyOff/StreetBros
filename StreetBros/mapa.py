import pygame
class MAP:
    def __init__(self, picture, max_x, min_x, max_y, min_y, sound):
        self.url = pygame.image.load(picture)
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y
        self.sound = sound
        
    def __str__(self):
        return self.url

class UdarEffect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.images = [udar1, udar2, udar3]
