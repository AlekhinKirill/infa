import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

def unicorn_right(screen, x, y, N, color):
  pygame.draw.ellipse(screen, color, (x, y, 150//N, 60//N))
  rect(screen, color, (x + 115//N, y - 40//N, 30//N, 60//N))
  circle(screen, color, (x + 140//N, y - 40//N), 15//N)
  pygame.draw.ellipse(screen, color, (x + 140//N, y - 45//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 110//N, y - 60//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 100//N, y - 50//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 90//N, y - 40//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 100//N, y - 20//N, 30//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x + 80//N, y - 20//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 85//N, y - 30//N, 35//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 70//N, y - 7//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x + 92//N, y - 25//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 90//N, y - 10//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x + 80//N, y - 15//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x + 83//N, y, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x + 107//N, y - 43//N, 27//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x + 95//N, y - 35//N, 20//N, 7//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x + 10//N, y, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x, y + 10//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 10//N, y + 20//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x, y + 40//N, 30//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 20//N, y + 40//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 15//N, y + 30//N, 35//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 30//N, y + 53//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 8//N, y + 35//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 10//N, y + 50//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 20//N, y + 45//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 17//N, y + 60//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x + 7//N, y + 17//N, 27//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 5//N, y + 25//N, 20//N, 7//N))
  rect(screen, color, (x + 105//N, y + 20//N, 10//N, 70//N))
  rect(screen, color, (x + 130//N, y + 40//N, 10//N, 70//N))
  rect(screen, color, (x + 35//N, y + 20//N, 10//N, 70//N))
  rect(screen, color, (x + 60//N, y + 40//N, 10//N, 70//N))
  circle(screen, (244, 148, 205), (x + 142//N, y - 42//N), 7//N)
  pygame.draw.ellipse(screen, (255, 255, 255), (x + 138//N, y - 42//N, 9//N, 2//N))
  circle(screen, (0, 0, 0), (x + 147//N, y - 42//N), 3//N)
  pygame.draw.polygon(screen, (157, 141, 207) , [[x + 132//N, y - 55//N], [x + 140//N, y - 55//N], [x + 145//N, y - 90//N]])


def unicorn_left(screen, x, y, N, color):
  x = x + 150//N
  pygame.draw.ellipse(screen, color, (x - 150//N, y, 150//N, 60//N))
  rect(screen, color, (x - 145//N, y - 40//N, 30//N, 60//N))
  circle(screen, color, (x - 140//N, y - 40//N), 15//N)
  pygame.draw.ellipse(screen, color, (x - 170//N, y - 45//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 140//N, y - 60//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 130//N, y - 50//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 130//N, y - 40//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 130//N, y - 20//N, 30//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 120//N, y - 20//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 120//N, y - 30//N, 35//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 110//N, y - 7//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 132//N, y - 25//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 130//N, y - 10//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 120//N, y - 15//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 123//N, y, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 134//N, y - 43//N, 27//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 115//N, y - 35//N, 20//N, 7//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 40//N, y, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 30//N, y + 10//N, 30//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 30//N, y + 20//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 30//N, y + 40//N, 30//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 20//N, y + 40//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 20//N, y + 30//N, 35//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 10//N, y + 53//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 32//N, y + 35//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (244, 148, 205), (x - 30//N, y + 50//N, 40//N, 15//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 20//N, y + 45//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 23//N, y + 60//N, 40//N, 10//N))
  pygame.draw.ellipse(screen, (157, 141, 207), (x - 20//N, y + 17//N, 27//N, 10//N))
  pygame.draw.ellipse(screen, (202, 123, 223), (x - 15//N, y + 25//N, 20//N, 7//N))
  rect(screen, color, (x - 115//N, y + 20//N, 10//N, 70//N))
  rect(screen, color, (x - 140//N, y + 40//N, 10//N, 70//N))
  rect(screen, color, (x - 45//N, y + 20//N, 10//N, 70//N))
  rect(screen, color, (x - 70//N, y + 40//N, 10//N, 70//N))
  circle(screen, (244, 148, 205), (x - 142//N, y - 42//N), 7//N)
  pygame.draw.ellipse(screen, (255, 255, 255), (x - 147//N, y - 42//N, 9//N, 2//N))
  circle(screen, (0, 0, 0), (x - 147//N, y - 42//N), 3//N)
  pygame.draw.polygon(screen, (157, 141, 207) , [[x - 132//N, y - 55//N], [x - 140//N, y - 55//N], [x - 145//N, y - 90//N]])


def tree(screen, color_leaves, color_apples, color_trunk, x, y, N):
  rect(screen, color_trunk, (x, y, 30//N, 100//N))
  pygame.draw.ellipse(screen, color_leaves, (x - 85//N, y - 150//N, 200//N, 100//N))
  pygame.draw.ellipse(screen, color_leaves, (x - 45//N, y - 230//N, 120//N, 150//N))
  pygame.draw.ellipse(screen, color_leaves, (x - 45//N, y - 80//N, 120//N, 100//N))
  circle(screen, color_apples, (x + 5//N, y - 180//N), 15//N)
  circle(screen, color_apples, (x + 50//N, y - 20//N), 15//N)
  circle(screen, color_apples, (x + 75//N, y - 90//N), 15//N)
  circle(screen, color_apples, (x - 45//N, y - 100//N), 15//N)

rect(screen, (9, 247, 207), (0, 0, 500, 500))
rect(screen, (19, 248, 8), (0, 170, 500, 400))
circle(screen, (225, 225, 0), (470, 40), 80)


tree(screen, (64, 109, 33), (244, 249, 23), (111, 23, 23), 30, 150, 3 )
tree(screen, (101, 170, 37), (255, 0, 0), (137, 109, 71), 190, 180, 3 )
tree(screen, (5, 70, 2), (244, 148, 205), (255, 255, 255), 95, 350, 1 )
unicorn_right(screen, 300, 370, 1, (170, 50, 80))
unicorn_left(screen, 220, 300, 2, (231, 246, 33))
unicorn_right(screen, 330, 250, 2, (170, 250, 250))
unicorn_right(screen, 260, 200, 3, (255, 255, 255))
unicorn_left(screen, 440, 200, 3, (181, 51, 233))
pygame.draw.line(screen, (225, 225, 0), [370, 60], [330, 70], 7)
pygame.draw.line(screen, (225, 225, 0), [370, 30], [325, 33], 7)
pygame.draw.line(screen, (225, 225, 0), [375, 90], [345, 110], 7)
pygame.draw.line(screen, (225, 225, 0), [400, 110], [370, 140], 7)
pygame.draw.line(screen, (225, 225, 0), [420, 135], [400, 160], 7)
pygame.draw.line(screen, (225, 225, 0), [450, 140], [440, 170], 7)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()