import pygame
import random
import time
from shooter import Shooter
from meteor import Meteor
from bullet import Bullet


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)
pygame.display.set_caption("Space Shooter!")
bg = pygame.image.load("space_background.jpg")
rocket = Shooter(460,860)
meteor = Meteor(120, 130)
size = (900, 1000)
bullet = Bullet(rocket.x, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True
yes = False

frame = 0
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rocket.move_right(10)
    if keys[pygame.K_a]:
        rocket.move_left(10)
    if keys[pygame.K_s]:
        yes = True
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    meteor.fall(7)

    bullet.fly(3)
    screen.blit(bullet.image, bullet.rect)
    screen.blit(bg, (0, 0))
    screen.blit(rocket.image, rocket.rect)
    screen.blit(meteor.image, meteor.rect)
    clock.tick(60)
    pygame.display.update()


    frame += 1


pygame.quit()



