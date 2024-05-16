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
begin_time = time.time()
rocket = Shooter(40,860)
meteor = Meteor(120, 130)
size = (900, 1000)
health = 3
how_to_play = "The goal of the game is to survive for as long as possible."
how_to_play_2 = "Every time a meteor hits your or passes you, you lose a life."
how_to_play_3 = "Shoot rockets at the meteors and make sure they don't pass you!"
how_to_play_4 = "Use \"a\" and \"d\" to move, and press space and \"s\" to shoot."
how_to_play_5 = "Press any key to start!"
lose_message = "HAHAHAHA YOU LOSE YOU FREAKING SUCK"
display_htp_message = my_font.render(how_to_play, True, (25, 255, 255))
display_htp_2_message = my_font.render(how_to_play_2, True, (25, 255, 255))
display_htp_3_message = my_font.render(how_to_play_3, True, (25, 255, 255))
display_htp_4_message = my_font.render(how_to_play_4, True, (25, 255, 255))
display_htp_5_message = my_font.render(how_to_play_5, True, (25, 255, 255))
display_lose = my_font.render(lose_message, True, (25, 255, 255))
display_health = my_font.render("Health: " + str(health), True, (25, 255, 255))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True
bullet1_release = False
released_1 = False
released_2 = False
bullet_2_release = False
test = 1
lose = False
start = False
frame = 0
while run:
    if not(lose) and start:
        current_time = time.time()
        stopwatch = current_time - begin_time
        stopwatch = round(stopwatch, 2)
        display_time = my_font.render("Time Elapsed: " + str(stopwatch), True, (25, 255, 255))
    display_health = my_font.render("Health: " + str(health), True, (25, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rocket.move_right(10)
        start = True
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        rocket.move_left(10)
        start = True
        test -= 1
    if keys[pygame.K_s]:
        if not(released_1):
            bullet_1 = Bullet(rocket.x - 92, 800)
        bullet1_release = True
        released_1 = True
        start = True
        test -= 1
    if keys[pygame.K_SPACE]:
        if not(released_2):
            bullet_2 = Bullet_2(rocket.x+20, 800)
        bullet_2_release = True
        start = True
        test -= 1
        released_2 = True
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    meteor.fall(10)
    if bullet1_release:
        bullet_1.fly(3)
    if bullet_2_release:
        bullet_2.fly(15)

    if meteor.rect.colliderect(rocket.rect):
        meteor.y = -10
        meteor.x = random.randint(80, 810)
        health -= 1

    if released_1:
        if meteor.rect.colliderect(bullet_1.rect):
            meteor.y = -10
            meteor.x = random.randint(80, 810)
    if released_2:
        if meteor.rect.colliderect(bullet_2.rect):
            meteor.y = -10
            meteor.x = random.randint(80, 810)


    if meteor.y >= 1200:
        meteor.y = -10
        meteor.x = random.randint(80, 810)
        health -= 1
    if health == 0:
        lose = True

    screen.blit(bg, (0, 0))
    if bullet1_release and not(lose):
        screen.blit(bullet_1.image, bullet_1.rect)
        if bullet_1.y < -230:
            released_1 = False
    if bullet_2_release and not(lose):
        screen.blit(bullet_2.image, bullet_2.rect)
        if bullet_2.y < -230:
            released_2 = False
    if not(lose) and start and (0 != test):
        screen.blit(rocket.image, rocket.rect)
        screen.blit(meteor.image, meteor.rect)
        screen.blit(display_time, (600, 70))
        screen.blit(display_health,(100, 70))
    elif not(start):
        screen.blit(display_htp_message, (140, 200))
        screen.blit(display_htp_2_message, (140, 250))
        screen.blit(display_htp_3_message, (140, 300))
        screen.blit(display_htp_4_message, (140, 350))
        screen.blit(display_htp_5_message, (140, 400))
    elif lose:
        screen.blit(display_lose, (220, 500))
        screen.blit(display_time, (350, 400))
    clock.tick(60)
    pygame.display.update()


    frame += 1


pygame.quit()



