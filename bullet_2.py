
import pygame

class Bullet_2:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.image = pygame.image.load("bullet_2.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def fly(self, speed):
        self.y -= speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])




