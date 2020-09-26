# infa
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (9, 247, 207), (0, 0, 500, 500))
rect(screen, (19, 248, 8), (0, 250, 500, 250))
circle(screen, (225, 225, 0), (500, 60), 80)
rect(screen, (255, 255, 255), (365, 230, 30, 60))
circle(screen, (255, 255, 255), (390, 230), 15)
pygame.draw.ellipse(screen, (255, 255, 255), (390, 225, 30, 15))
rect(screen, (255, 255, 255), (95, 350, 30, 100))
pygame.draw.ellipse(screen, (255, 255, 255), (250, 270, 150, 60))
pygame.draw.ellipse(screen, (5, 70, 2), (10, 200, 200, 100))
pygame.draw.ellipse(screen, (5, 70, 2), (50, 120, 120, 150))
pygame.draw.ellipse(screen, (5, 70, 2), (50, 270, 120, 100))
circle(screen, (244, 148, 205), (100, 170), 15)
circle(screen, (244, 148, 205), (145, 330), 15)
circle(screen, (244, 148, 205), (170, 260), 15)
circle(screen, (244, 148, 205), (50, 250), 15)
pygame.draw.ellipse(screen, (244, 148, 205), (360, 210, 30, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (350, 220, 30, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (340, 230, 40, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (350, 250, 30, 10))
pygame.draw.ellipse(screen, (202, 123, 223), (330, 250, 40, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (335, 240, 35, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (320, 263, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (342, 245, 40, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (340, 260, 40, 15))
pygame.draw.ellipse(screen, (157, 141, 207), (330, 255, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (333, 270, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (357, 227, 27, 10))
pygame.draw.ellipse(screen, (202, 123, 223), (345, 235, 20, 7))

pygame.draw.ellipse(screen, (244, 148, 205), (260, 270, 30, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (250, 280, 30, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (240, 290, 40, 15))
pygame.draw.ellipse(screen, (244, 148, 205), (250, 310, 30, 10))
pygame.draw.ellipse(screen, (202, 123, 223), (230, 310, 40, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (235, 300, 35, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (220, 323, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (242, 305, 40, 10))
pygame.draw.ellipse(screen, (244, 148, 205), (240, 320, 40, 15))
pygame.draw.ellipse(screen, (157, 141, 207), (230, 315, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (233, 330, 40, 10))
pygame.draw.ellipse(screen, (157, 141, 207), (257, 287, 27, 10))
pygame.draw.ellipse(screen, (202, 123, 223), (245, 295, 20, 7))
rect(screen, (255, 255, 255), (355, 290, 10, 70))
rect(screen, (255, 255, 255), (380, 310, 10, 70))
rect(screen, (255, 255, 255), (285, 290, 10, 70))
rect(screen, (255, 255, 255), (310, 310, 10, 70))
circle(screen, (244, 148, 205), (392, 228), 7)
pygame.draw.ellipse(screen, (255, 255, 255), (388, 228, 9, 2))
circle(screen, (0, 0, 0), (397, 228), 3)
pygame.draw.polygon(screen, (157, 141, 207) , [[382, 215], [390, 215], [395, 180]])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
