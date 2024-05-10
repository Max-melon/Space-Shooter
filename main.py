import pygame
import random
import time
from shooter import Shooter
from meteor import Meteor
from bullet import Bullet
from bullet_2 import Bullet_2

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)
pygame.display.set_caption("Space Shooter!")
bg = pygame.image.load("space_background.jpg")
rocket = Shooter(40,860)
meteor = Meteor(120, 130)
size = (900, 1000)
message = "Shoot rockets at the meteors and make sure they don't pass you!"
display_message = my_font.render(message, True, (25, 255, 255))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True
bullet1_release = False
released_1 = False
released_2 = False
bullet_2_release = False
frame = 0
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rocket.move_right(10)
    if keys[pygame.K_a]:
        rocket.move_left(10)
    if keys[pygame.K_s]:
        if not(released_1):
            bullet_1 = Bullet(rocket.x - 92, 800)
        bullet1_release = True
        released_1 = True
    if keys[pygame.K_SPACE]:
        if not(released_2):
            bullet_2 = Bullet_2(rocket.x+20, 800)
        bullet_2_release = True
        released_2 = True
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    meteor.fall(7)
    if bullet1_release:
        bullet_1.fly(3)
    if bullet_2_release:
        bullet_2.fly(15)

    screen.blit(bg, (0, 0))
    if bullet1_release:
        screen.blit(bullet_1.image, bullet_1.rect)
        if bullet_1.y < -230:
            released_1 = False
    if bullet_2_release:
        screen.blit(bullet_2.image, bullet_2.rect)
        if bullet_2.y < -230:
            released_2 = False
    screen.blit(rocket.image, rocket.rect)
    screen.blit(meteor.image, meteor.rect)
    screen.blit(display_message, (140, 200))
    clock.tick(60)
    pygame.display.update()


    frame += 1


pygame.quit()



