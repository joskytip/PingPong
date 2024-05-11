import pygame.time
from pygame import *
from Shooter.PingPong.Player import Player
from Shooter.PingPong.GameSprite import GameSprite
palka = Player
window = display.set_mode((850, 600))
display.set_caption("ПингПонг")

background = transform.scale(image.load("oi oi oi.jpg"), (850, 600))

x1, y1 = 50, 500
x2, y2 = 750, 500
x3, y3 = 375, 250

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (255,0,0))

font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True, (255,0,0))

palka1 = Player("shrek.jpeg", x1, y1, 10, (65, 65),window)
palka2 = Player("shrek.jpeg", x2, y2, 10, (65, 65),window)
ball = GameSprite("круг.jpg", x3, y3, 10, (30, 30), window)
FPS = 60
clock = time.Clock()

game = True
finish = False

speed_x = 3
speed_y = 3

while game:
    # Установка ФПС
    clock.tick(FPS)
    window.blit(background, (0, 0))

    for e in event.get():

        if e.type == QUIT:
            game = False

        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if ball.rect.y > 600-50 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200, 200))

        if ball.rect.x > 850-50:
            finish = True
            window.blit(lose2,(200, 200))

        if sprite.collide_rect(palka1, ball) or sprite.collide_rect(palka2, ball):
            speed_x *= -1

    palka1.reset()
    palka1.update_l()

    palka2.reset()
    palka2.update_r()

    ball.reset()
    ball.update()

    display.update()



