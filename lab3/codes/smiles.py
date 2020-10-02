import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
a = 200

circle(screen, (225, 225, 0), (a, 175), 150)
circle(screen, (255, 0, 0), (a - 80, 150), 40)
circle(screen, (255, 0, 0), (a + 80, 150), 40)
circle(screen, (0, 0, 0), (a + 80, 150), 20)
circle(screen, (0, 0, 0), (a - 80, 150), 20)
rect(screen, (0, 0, 0), (a - 80, 230, 150, 30))
polygon(screen, (0, 0, 0,), [[a + 40, 140], [a + 20, 120], [a + 110, 80], [a + 100, 100]])
polygon(screen, (0, 0, 0,), [[a -40, 140], [a -20, 120], [a -110, 80], [a - 100, 100]])
a = a + 400
circle(screen, (225, 225, 0), (a, 175), 150)
circle(screen, (0, 200, 0), (a - 80, 150), 40)
circle(screen, (0, 200, 64), (a + 80, 150), 40)
circle(screen, (0, 0, 0), (a + 80, 150), 20)
circle(screen, (0, 0, 0), (a - 80, 150), 20)
rect(screen, (0, 0, 0), (a - 80, 230, 150, 30))
polygon(screen, (0, 0, 0,), [[a - 110, 140], [a - 130, 120], [a - 40, 80], [a - 50, 100]])
polygon(screen, (0, 0, 0,), [[a + 110, 140], [a + 130, 120], [a + 40, 80], [a + 50, 100]])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()