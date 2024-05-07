import pygame
import random
import time
from shooter import Shooter

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)
pygame.display.set_caption("Space Shooter!")
bg = pygame.image.load("space_background.jpg")
rocket = Shooter(460,40)

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True

frame = 0
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rocket.move_right(10)



    clock.tick(60)
    screen.blit(bg, (0, 0))
    screen.blit(rocket.image, rocket.rect)
    pygame.display.update()


    frame += 1


pygame.quit()



