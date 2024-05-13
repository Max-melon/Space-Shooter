import pygame
import random

class Meteor:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.image = pygame.image.load("meteor.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def fall(self, speed):
        self.y += speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
