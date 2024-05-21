import pygame

class Boss:

    def __init__(self, x, y, health):
        self.y = y
        self.x = x
        self.health = health
        self.image = pygame.image.load("boss.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, speed, repeat):
        for i in range(repeat):
            for i in range(3):
                self.x += speed
            for i in range(3):
                self.x -= speed


