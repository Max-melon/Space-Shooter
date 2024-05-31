import pygame
import random

class Egg:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.image = pygame.image.load("egg.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

    def fall(self, speed):
        self.y += speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])