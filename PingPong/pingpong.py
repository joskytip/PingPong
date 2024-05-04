import pygame.time
from pygame import *
from Shooter.PingPong.Player import Player

palka = Player
window = display.set_mode((850, 600))
display.set_caption("ПингПонг")

background = transform.scale(image.load("oi oi oi.jpg"), (850, 600))

x1, y1 = 50, 500
x2, y2 = 750, 500

palka1 = Player("shrek.jpeg", x1, y1, 10, (65, 65),window)
palka2 = Player("shrek.jpeg", x2, y2, 10, (65, 65),window)
FPS = 60
clock = time.Clock()

game = True
finish = False

while game:
    # Установка ФПС
    clock.tick(FPS)
    window.blit(background, (0, 0))

    for e in event.get():

        if e.type == QUIT:
            game = False

    palka1.reset()
    palka1.update_l()

    palka2.reset()
    palka2.update_r()

    display.update()

