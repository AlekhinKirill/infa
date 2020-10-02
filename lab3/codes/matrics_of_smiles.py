import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
a = 200
b = 175

print('Введите целое число (половину размера плитки)')
N = int(input())
for i in range(1,N + 1):
  for j in range(1, N + 1): 
    circle(screen, (225, 225, 0), (a//N, b//N), 150//N)
    circle(screen, (255, 0, 0), ((a - 80)//N, (b - 25)//N), 40//N)
    circle(screen, (255, 0, 0), ((a + 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 0, 0), ((a + 80)//N, (b - 25)//N), 20//N)
    circle(screen, (0, 0, 0), ((a - 80)//N, (b - 25)//N), 20//N)
    rect(screen, (0, 0, 0), ((a - 80)//N,(b + 55)//N , 150//N, 30//N))
    polygon(screen, (0, 0, 0), [[(a + 40)//N, (b - 35)//N], [(a + 20)//N, (b - 55)//N], [(a + 110)//N, (b - 95)//N], [(a + 100)//N, (b - 75)//N]])
    polygon(screen, (0, 0, 0,), [[(a - 40)//N, (b - 35)//N], [(a - 20)//N, (b - 55)//N], [(a - 110)//N, (b - 95)//N], [(a - 100)//N, (b - 75)//N]])
    a = a + 400
    circle(screen, (225, 225, 0), (a//N, b//N), 150//N)
    circle(screen, (0, 200, 0), ((a - 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 200, 64), ((a + 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 0, 0), ((a + 80)//N, (b - 25)//N), 20//N)
    circle(screen, (0, 0, 0), ((a - 80)//N, (b - 25)//N), 20//N)
    rect(screen, (0, 0, 0), ((a - 80)//N, (b + 55)//N, 150//N, 30//N))
    polygon(screen, (0, 0, 0,), [[(a - 110)//N, (b - 35)//N], [(a - 130)//N, (b - 55)//N], [(a - 40)//N, (b - 95)//N], [(a - 50)//N, (b - 75)//N]])
    polygon(screen, (0, 0, 0,), [[(a + 110)//N, (b - 35)//N], [(a + 130)//N, (b - 55)//N], [(a + 40)//N, (b - 95)//N], [(a + 50)//N, (b - 75)//N]])
    a = a + 400
  a = 200
  b = b + 400
  for j in range(1, N + 1):
    circle(screen, (225, 225, 0), (a//N, b//N), 150//N)
    circle(screen, (0, 200, 0), ((a - 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 200, 64), ((a + 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 0, 0), ((a + 80)//N, (b - 25)//N), 20//N)
    circle(screen, (0, 0, 0), ((a - 80)//N, (b - 25)//N), 20//N)
    rect(screen, (0, 0, 0), ((a - 80)//N, (b + 55)//N, 150//N, 30//N))
    polygon(screen, (0, 0, 0,), [[(a - 110)//N, (b - 35)//N], [(a - 130)//N, (b - 55)//N], [(a - 40)//N, (b - 95)//N], [(a - 50)//N, (b - 75)//N]])
    polygon(screen, (0, 0, 0,), [[(a + 110)//N, (b - 35)//N], [(a + 130)//N, (b - 55)//N], [(a + 40)//N, (b - 95)//N], [(a + 50)//N, (b - 75)//N]])
    a = a + 400
    circle(screen, (225, 225, 0), (a//N, b//N), 150//N)
    circle(screen, (255, 0, 0), ((a - 80)//N, (b - 25)//N), 40//N)
    circle(screen, (255, 0, 0), ((a + 80)//N, (b - 25)//N), 40//N)
    circle(screen, (0, 0, 0), ((a + 80)//N, (b - 25)//N), 20//N)
    circle(screen, (0, 0, 0), ((a - 80)//N, (b - 25)//N), 20//N)
    rect(screen, (0, 0, 0), ((a - 80)//N,(b + 55)//N , 150//N, 30//N))
    polygon(screen, (0, 0, 0), [[(a + 40)//N, (b - 35)//N], [(a + 20)//N, (b - 55)//N], [(a + 110)//N, (b - 95)//N], [(a + 100)//N, (b - 75)//N]])
    polygon(screen, (0, 0, 0,), [[(a - 40)//N, (b - 35)//N], [(a - 20)//N, (b - 55)//N], [(a - 110)//N, (b - 95)//N], [(a - 100)//N, (b - 75)//N]])
    a = a + 400
  a = 200
  b = b + 400
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()