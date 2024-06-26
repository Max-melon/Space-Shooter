import pygame

class Boss:

    def __init__(self, x, y, health):
        self.y = y
        self.x = x
        self.health = health
        self.image = pygame.image.load("boss.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

    def move_right(self, speed):
        self.x += speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_left(self, speed):
        self.x -= speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

