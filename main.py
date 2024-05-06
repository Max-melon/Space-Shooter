import pygame
import random
import time

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)
pygame.display.set_caption("Space Shooter!")
bg = pygame.image.load("space_background.jpg")


size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True

frame = 0
while run:
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pygame.display.update()


    frame += 1


pygame.quit()



