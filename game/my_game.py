import pygame
import time
from random import randint

pygame.init()
win = pygame.display.set_mode((800, 600))
bg = pygame.image.load('bd.jpg').convert()
ship = pygame.image.load('ship.png').convert()
ship.set_colorkey((255, 255, 255))
enemy_ship = pygame.image.load('ship3.png').convert()
enemy_ship = pygame.transform.rotate(enemy_ship, 180)
enemy_ship.set_colorkey((255, 255, 255))
boom = pygame.image.load('boom.png').convert()
boom.set_colorkey((255, 255, 255))
asteroid = pygame.image.load('asteroid2.png').convert()
asteroid.set_colorkey((255, 255, 255))
asteroid_x, asteroid_y = 0, 265
asteroid2 = pygame.image.load('asteroid2.png').convert()
asteroid2.set_colorkey((255, 255, 255))
asteroid2_x, asteroid2_y = 244, 265
asteroid3 = pygame.image.load('asteroid2.png').convert()
asteroid3.set_colorkey((255, 255, 255))
asteroid3_x, asteroid3_y = 498, 265
asteroid4 = pygame.image.load('asteroid2.png').convert()
asteroid4.set_colorkey((255, 255, 255))
asteroid4_x, asteroid4_y = 687, 265
pygame.mouse.set_visible(False)
bullets_in_game = []
win.blit(bg, (0, 0))
player_alive = True
enemy_alive = True
x_en_1, y_en_1 = 100, 150
enemy_alive2 = True
x_en_2, y_en_2 = 250, 150
enemy_alive3 = True
x_en_3, y_en_3 = 400, 150
enemy_alive4 = True
x_en_4, y_en_4 = 550, 150
enemy_alive5 = True
x_en_5, y_en_5 = 700, 150
enemy_alive6 = True
x_en_6, y_en_6 = 175, 50
enemy_alive7 = True
x_en_7, y_en_7 = 325, 50
enemy_alive8 = True
x_en_8, y_en_8 = 475, 50
enemy_alive9 = True
x_en_9, y_en_9 = 625, 50
fire = False
x = 0
y = 0



def launch(x, y):
    pygame.draw.circle(win, (255, 0, 0), (x, y - 50), 10)
    if y == 50:
        bullets_in_game.pop(0)
    elif (asteroid_x < x < (asteroid_x + 113)) and y == (asteroid_y + 150):
        bullets_in_game.pop(0)


def enemy_1(x, y):
    win.blit(enemy_ship, (100, 150))
    if (100 < x < 133) and y == 230:
        win.blit(boom, (100, 150))
        global enemy_alive
        enemy_alive = False
        bullets_in_game.pop(0)
def enemy_2(x, y):
    win.blit(enemy_ship, (250, 150))
    if (250 < x < 283) and y == 230:
        win.blit(boom, (250, 150))
        global enemy_alive2
        enemy_alive2 = False
        bullets_in_game.pop(0)
def enemy_3(x, y):
    win.blit(enemy_ship, (400, 150))
    if (400 < x < 433) and y == 230:
        win.blit(boom, (400, 150))
        global enemy_alive3
        enemy_alive3 = False
        bullets_in_game.pop(0)
def enemy_4(x, y):
    win.blit(enemy_ship, (550, 150))
    if (550 < x < 683) and y == 230:
        win.blit(boom, (550, 150))
        global enemy_alive4
        enemy_alive4 = False
        bullets_in_game.pop(0)
def enemy_5(x, y):
    win.blit(enemy_ship, (700, 150))
    if (700 < x < 733) and y == 230:
        win.blit(boom, (700, 150))
        global enemy_alive5
        enemy_alive5 = False
        bullets_in_game.pop(0)
def enemy_6(x, y):
    win.blit(enemy_ship, (175, 50))
    if (175 < x < 208) and y == 130:
        win.blit(boom, (175, 50))
        global enemy_alive6
        enemy_alive6 = False
        bullets_in_game.pop(0)
def enemy_7(x, y):
    win.blit(enemy_ship, (325, 50))
    if (325 < x < 358) and y == 130:
        win.blit(boom, (325, 50))
        global enemy_alive7
        enemy_alive7 = False
        bullets_in_game.pop(0)
def enemy_8(x, y):
    win.blit(enemy_ship, (475, 50))
    if (475 < x < 508) and y == 130:
        win.blit(boom, (475, 50))
        global enemy_alive8
        enemy_alive8 = False
        bullets_in_game.pop(0)
def enemy_9(x, y):
    win.blit(enemy_ship, (625, 50))
    if (625 < x < 658) and y == 130:
        win.blit(boom, (625, 50))
        global enemy_alive9
        enemy_alive9 = False
        bullets_in_game.pop(0)

def enemy_bullet(x, y):
    pygame.draw.circle(win, (255, 0, 0), (x + 16, y + 33), 10)
def enemy_bullet2(x, y):
    pygame.draw.circle(win, (255, 0, 0), (x + 16, y + 33), 10)


while True:
    win.blit(bg, (0, 0))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if len(bullets_in_game) == 0:
                    bullets_in_game.append(1)
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    #launch(x, y)
                    fire = True

    pos = pygame.mouse.get_pos()

    if fire and len(bullets_in_game) > 0:
        win.blit(bg, (0, 0))
        y -= 1
        launch(x, y)

    if enemy_alive:
        enemy_1(x, y)
        enemy_bullet(x_en_1, y_en_1)
        y_en_1 += 1
        if y_en_1 == 600:
            y_en_1 = 150
        elif (pos[0] - 45) < x_en_1 < (pos[0] + 45) and y_en_1 == pos[1] - 70:
            y_en_1 = 150
            player_alive = False
        elif (asteroid_x < x_en_1 < (asteroid_x + 113)) and y_en_1 == asteroid_y:
            y_en_1 = 150
        elif (asteroid2_x < x_en_1 < (asteroid2_x + 113)) and y_en_1 == asteroid2_y:
            y_en_1 = 150
        elif (asteroid3_x < x_en_1 < (asteroid3_x + 113)) and y_en_1 == asteroid3_y:
            y_en_1 = 150
        elif (asteroid4_x < x_en_1 < (asteroid4_x + 113)) and y_en_1 == asteroid4_y:
            y_en_1 = 150
    if enemy_alive2:
        enemy_2(x, y)
        enemy_bullet(x_en_2, y_en_2)
        y_en_2 += 1
        if y_en_2 == 600:
            y_en_2 = 150
        elif (pos[0] - 45) < x_en_2 < (pos[0] + 45) and y_en_2 == pos[1] - 70:
            y_en_2 = 150
            player_alive = False
        elif (asteroid_x < x_en_2 < (asteroid_x + 113)) and y_en_2 == asteroid_y:
            y_en_2 = 150
        elif (asteroid2_x < x_en_2 < (asteroid2_x + 113)) and y_en_2 == asteroid2_y:
            y_en_2 = 150
        elif (asteroid3_x < x_en_2 < (asteroid3_x + 113)) and y_en_2 == asteroid3_y:
            y_en_2 = 150
        elif (asteroid4_x < x_en_2 < (asteroid4_x + 113)) and y_en_2 == asteroid4_y:
            y_en_2 = 150
    if enemy_alive3:
        enemy_3(x, y)
        enemy_bullet(x_en_3, y_en_3)
        y_en_3 += 1
        if y_en_3 == 600:
            y_en_3 = 150
        elif (pos[0] - 45) < x_en_3 < (pos[0] + 45) and y_en_3 == pos[1] - 70:
            y_en_3 = 150
            player_alive = False
        elif (asteroid_x < x_en_3 < (asteroid_x + 113)) and y_en_3 == asteroid_y:
            y_en_3 = 150
        elif (asteroid2_x < x_en_3 < (asteroid2_x + 113)) and y_en_3 == asteroid2_y:
            y_en_3 = 150
        elif (asteroid3_x < x_en_3 < (asteroid3_x + 113)) and y_en_3 == asteroid3_y:
            y_en_3 = 150
        elif (asteroid4_x < x_en_3 < (asteroid4_x + 113)) and y_en_3 == asteroid4_y:
            y_en_3 = 150
    if enemy_alive4:
        enemy_4(x, y)
        enemy_bullet(x_en_4, y_en_4)
        y_en_4 += 1
        if y_en_4 == 600:
            y_en_4 = 150
        elif (pos[0] - 45) < x_en_4 < (pos[0] + 45) and y_en_4 == pos[1] - 70:
            y_en_4 = 150
            player_alive = False
        elif (asteroid_x < x_en_4 < (asteroid_x + 113)) and y_en_4 == asteroid_y:
            y_en_4 = 150
        elif (asteroid2_x < x_en_4 < (asteroid2_x + 113)) and y_en_4 == asteroid2_y:
            y_en_4 = 150
        elif (asteroid3_x < x_en_4 < (asteroid3_x + 113)) and y_en_4 == asteroid3_y:
            y_en_4 = 150
        elif (asteroid4_x < x_en_4 < (asteroid4_x + 113)) and y_en_4 == asteroid4_y:
            y_en_4 = 150
    if enemy_alive5:
        enemy_5(x, y)
        enemy_bullet(x_en_5, y_en_5)
        y_en_5 += 1
        if y_en_5 == 600:
            y_en_5 = 150
        elif (pos[0] - 45) < x_en_5 < (pos[0] + 45) and y_en_5 == pos[1] - 70:
            y_en_5 = 150
            player_alive = False
        elif (asteroid_x < x_en_5 < (asteroid_x + 113)) and y_en_5 == asteroid_y:
            y_en_5 = 150
        elif (asteroid2_x < x_en_5 < (asteroid2_x + 113)) and y_en_5 == asteroid2_y:
            y_en_4 = 150
        elif (asteroid3_x < x_en_5 < (asteroid3_x + 113)) and y_en_5 == asteroid3_y:
            y_en_5 = 150
        elif (asteroid4_x < x_en_5 < (asteroid4_x + 113)) and y_en_5 == asteroid4_y:
            y_en_5 = 150
    if enemy_alive6:
        enemy_6(x, y)
        enemy_bullet2(x_en_6, y_en_6)
        y_en_6 += 1
        if y_en_6 == 600:
            y_en_6 = 50
        elif (pos[0] - 45) < x_en_6 < (pos[0] + 45) and y_en_6 == pos[1] - 70:
            y_en_6 = 50
            player_alive = False
        elif (asteroid_x < x_en_6 < (asteroid_x + 113)) and y_en_6 == asteroid_y:
            y_en_6 = 50
        elif (asteroid2_x < x_en_6 < (asteroid2_x + 113)) and y_en_6 == asteroid2_y:
            y_en_6 = 50
        elif (asteroid3_x < x_en_6 < (asteroid3_x + 113)) and y_en_6 == asteroid3_y:
            y_en_6 = 50
        elif (asteroid4_x < x_en_6 < (asteroid4_x + 113)) and y_en_6 == asteroid4_y:
            y_en_6 = 50
    if enemy_alive7:
        enemy_7(x, y)
        enemy_bullet2(x_en_7, y_en_7)
        y_en_7 += 1
        if y_en_7 == 600:
            y_en_7 = 50
        elif (pos[0] - 45) < x_en_7 < (pos[0] + 45) and y_en_7 == pos[1] - 70:
            y_en_7 = 50
            player_alive = False
        elif (asteroid_x < x_en_7 < (asteroid_x + 113)) and y_en_7 == asteroid_y:
            y_en_7 = 50
        elif (asteroid2_x < x_en_7 < (asteroid2_x + 113)) and y_en_7 == asteroid2_y:
            y_en_7 = 50
        elif (asteroid3_x < x_en_7 < (asteroid3_x + 113)) and y_en_7 == asteroid3_y:
            y_en_7 = 50
        elif (asteroid4_x < x_en_7 < (asteroid4_x + 113)) and y_en_7 == asteroid4_y:
            y_en_7 = 50
    if enemy_alive8:
        enemy_8(x, y)
        enemy_bullet2(x_en_8, y_en_8)
        y_en_8 += 1
        if y_en_8 == 600:
            y_en_8 = 50
        elif (pos[0] - 45) < x_en_8 < (pos[0] + 45) and y_en_8 == pos[1] - 70:
            y_en_8 = 50
            player_alive = False
        elif (asteroid_x < x_en_8 < (asteroid_x + 113)) and y_en_8 == asteroid_y:
            y_en_8 = 50
        elif (asteroid2_x < x_en_8 < (asteroid2_x + 113)) and y_en_8 == asteroid2_y:
            y_en_8 = 50
        elif (asteroid3_x < x_en_8 < (asteroid3_x + 113)) and y_en_8 == asteroid3_y:
            y_en_8 = 50
        elif (asteroid4_x < x_en_8 < (asteroid4_x + 113)) and y_en_8 == asteroid4_y:
            y_en_8 = 50
    if enemy_alive9:
        enemy_9(x, y)
        enemy_bullet2(x_en_9, y_en_9)
        y_en_9 += 1
        if y_en_9 == 600:
            y_en_9 = 50
        elif (pos[0] - 45) < x_en_9 < (pos[0] + 45) and y_en_9 == pos[1] - 70:
            y_en_9 = 50
            player_alive = False
        elif (asteroid_x < x_en_9 < (asteroid_x + 113)) and y_en_9 == asteroid_y:
            y_en_9 = 50
        elif (asteroid2_x < x_en_9 < (asteroid2_x + 113)) and y_en_9 == asteroid2_y:
            y_en_9 = 50
        elif (asteroid3_x < x_en_9 < (asteroid3_x + 113)) and y_en_9 == asteroid3_y:
            y_en_9 = 50
        elif (asteroid4_x < x_en_9 < (asteroid4_x + 113)) and y_en_9 == asteroid4_y:
            y_en_9 = 50


    #pygame.draw.rect(win, (0, 255, 0), (100, 183, 30, 30))
    pos = pygame.mouse.get_pos()
    if player_alive:
        win.blit(ship, (pos[0] - 50, pos[1] - 50))

    win.blit(asteroid, (asteroid_x, asteroid_y))
    asteroid_x += 1
    if asteroid_x == 800:
        asteroid_x = -113
    win.blit(asteroid2, (asteroid2_x, asteroid2_y))
    asteroid2_x += 1
    if asteroid2_x == 800:
        asteroid2_x = -113
    win.blit(asteroid3, (asteroid3_x, asteroid3_y))
    asteroid3_x += 1
    if asteroid3_x == 800:
        asteroid3_x = -113
    win.blit(asteroid4, (asteroid4_x, asteroid4_y))
    asteroid4_x += 1
    if asteroid4_x == 800:
        asteroid4_x = -113

    pygame.display.update()
    pygame.time.delay(10)