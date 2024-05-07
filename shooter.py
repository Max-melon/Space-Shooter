import pygame


class Shooter:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.image = pygame.image.load("rocket.jpg")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_left(self, new_x):
        self.x -= new_x
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_right(self, new_x):
        self.x += new_x
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

