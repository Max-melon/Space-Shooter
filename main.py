import pygame
import random
import time
from shooter import Shooter
from meteor import Meteor
from bullet import Bullet
from bullet_2 import Bullet_2
from boss import Boss
from egg import Egg


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)
better_font = pygame.font.SysFont('Comic Sans', 30)
pygame.display.set_caption("Space Shooter!")
bg = pygame.image.load("space_background.jpg")

rocket = Shooter(40,860)
meteor = Meteor(320, 0)
size = (900, 1000)
health = 3
boss = Boss(250, 100, 500)
egg = Egg(1000,100)

how_to_play = "The goal of the game is to survive for as long as possible."
how_to_play_2 = "Every time a meteor hits your or passes you, you lose a life."
how_to_play_3 = "Shoot rockets at the meteors and make sure they don't pass you!"
how_to_play_4 = "Use \"a\" and \"d\" to move, and press space and left click to shoot."
how_to_play_5 = "Press \"a\" or \"d\" to start!"
lose_message = "HAHAHAHA YOU LOSE YOU FREAKING SUCK"
win_message = "GOOD JOB YOU WIN!"

display_htp_message = my_font.render(how_to_play, True, (25, 255, 255))
display_htp_2_message = my_font.render(how_to_play_2, True, (25, 255, 255))
display_htp_3_message = my_font.render(how_to_play_3, True, (25, 255, 255))
display_htp_4_message = my_font.render(how_to_play_4, True, (25, 255, 255))
display_htp_5_message = my_font.render(how_to_play_5, True, (25, 255, 255))
display_lose = my_font.render(lose_message, True, (255, 25, 25))
display_health = my_font.render("Health: " + str(health), True, (25, 255, 255))
display_win = better_font.render(win_message, True, (25, 255, 25))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

direction = True
run = True
bullet_1_release = False
released_1 = False
released_2 = False
bullet_2_release = False
test = 1
lose = False
boss_start = False
start = False
frame = 0
check = True
count = True
win = False

while run:
    if start and check:
        begin_time = time.time()
        check = False
    if not(lose) and start:
        current_time = time.time()
        stopwatch = current_time - begin_time
        stopwatch = round(stopwatch, 2)
        display_time = my_font.render("Time Elapsed: " + str(stopwatch), True, (25, 255, 255))
    display_health = my_font.render("Health: " + str(health), True, (25, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rocket.move_right(5)
        start = True
        test -= 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        rocket.move_left(5)
        start = True
        test -= 1
    if keys[pygame.K_SPACE]:
        if not(released_1):
            bullet_1 = Bullet(rocket.x - 92, 800)
        bullet_1_release = True
        released_1 = True
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not (released_2):
                bullet_2 = Bullet_2(rocket.x + 20, 800)
            bullet_2_release = True
            released_2 = True

    if start:
        meteor.fall(5.5)
    if bullet_1_release:
        bullet_1.fly(1.5)
    if bullet_2_release:
        bullet_2.fly(7.5)
    if boss_start:
        egg.fall(20)

    if boss_start:
        # print(bullet_2.image)
        if (round(((stopwatch * 100) % 100), 0) == 0 and count) and direction:
            boss.move_right(200)
            count = False
            direction = False
        elif (round(((stopwatch * 100) % 100), 0) == 0 and count) and not(direction):
            boss.move_left(200)
            count = False
            direction = True
        elif round(((stopwatch * 100) % 100), 0) == 99:
            egg.x = boss.x
            egg.y = boss.y
            count = True

        if count:
            egg.fall(20)

    if meteor.rect.colliderect(rocket.rect) and not(boss_start):
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
            bullet_2.y = 100000000


    if meteor.y >= 1200 and not(boss_start):
        meteor.y = -10
        meteor.x = random.randint(80, 810)
        health -= 1
    if boss_start and not(lose):
        if egg.rect.colliderect(rocket.rect) and boss_start:
            health -= 1
            egg.y = 10000
        elif egg.rect.colliderect(bullet_2.rect) and boss_start:
            egg.y = 10000
            bullet_2.y = -100000
        elif bullet_2.rect.colliderect(boss.rect) and boss_start:
            bullet_2.y = 10000
            boss.health -= 50
            boss_health = my_font.render("Boss Health: " + str(boss.health), True, (255, 25, 255))
    if health == 0:
        lose = True

    if start and test <= -1:
        if stopwatch >= 30 and not(boss_start):
            boss_health = my_font.render("Boss Health: " + str(boss.health), True, (255, 25, 255))
            boss_start = True
            health = 3

    if boss.health == 0:
        boss_start = False
        win = True

    screen.blit(bg, (0, 0))
    if bullet_1_release and (not(lose) and not(boss_start)):
        screen.blit(bullet_1.image, bullet_1.rect)
        if bullet_1.y < -230:
            released_1 = False
    if bullet_2_release and not(lose) and not win:
        screen.blit(bullet_2.image, bullet_2.rect)
        if bullet_2.y < -230:
            released_2 = False
        elif bullet_2.y > 1000:
            released_2 = False
    if boss_start and not(lose):
        screen.blit(rocket.image, rocket.rect)
        screen.blit(boss.image, boss.rect)
        screen.blit(display_health, (100, 70))
        screen.blit(egg.image, egg.rect)
        screen.blit(boss_health, (720, 70))
    elif win:
        screen.blit(display_win, (280, 400))
    elif not(lose) and start and (0 != test):
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
    clock.tick(120)
    pygame.display.update()


    frame += 1


pygame.quit()



