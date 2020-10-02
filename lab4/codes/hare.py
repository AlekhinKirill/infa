import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_mouth(surface, x, y, width, height):
    '''
    Функция рисует рот зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина рта
    {int} height - высота рта

    Возвращаемые значения:
    Выводит рот зайца на экран
    '''
    pi = 3.14
    arc(surface, [0, 0, 0], (x, y, width, height), pi, 7*pi/4, 3)
    arc(surface, [0, 0, 0], (x - width, y, width, height), 5*pi/4, 2*pi,3)

def draw_nose(surface, x, y, width, color_nose):
     '''
    Функция рисует нос зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина носа
    {int} height - высота носа
    {tuple} color_nose - цвет носа

    Возвращаемые значения:
    Выводит нос зайца на экран
    '''
     polygon(screen, color_nose, [(x, y - width), (x - width//2 ,y - 3*width//2), (x + width//2 ,y - 3*width//2)])

def draw_body(surface, x, y, width, height, color):
    '''
    Функция рисует тело зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина туловища
    {int} height - высота туловища
    {tuple} color - цвет туловища

    Возвращаемые значения:
    Выводит живот зайца на экран
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    ellipse(surface, [255, 255, 255], (x - width // 3, y - height // 3, 2*width//3, 2*height//3))


def draw_head(surface, x, y, size, color):
    '''
    Функция рисует голову зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} size - размер головы
    {tuple} color - цвет головы

    Возвращаемые значения:
    Выводит голову зайца на экран
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Функция рисует уши зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина ушей
    {int} height - выысота ушей

    Возвращаемые значения:
    Выводит голову зайца на экран
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Функция рисует ноги зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина ушей
    {int} height - выысота ушей
    {tuple} color - цвет ног

    Возвращаемые значения:
    Выводит голову ноги на экран
    '''
  
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_eyes (surface, x, y, width, height, size):
    '''
    Функция рисует глаза зайца.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина глаз
    {int} height - высота глаз
    {int} size - размер зрачка

    Возвращаемые значения:
    Выводит ноги на экран
    '''
    ellipse(surface, [255, 255, 255], (x - width//2, y - 4*height//3, width, height))
    ellipse(surface, [255, 255, 255], (x + width//2, y - 4*height//3, width, height))
    circle(surface, [0, 0, 0], (x + width, y - height), size)
    circle(surface, [0, 0, 0], (x, y - height), size)


def draw_hare(surface, x, y, width, height, color):
    '''
    Функция рисует(собирает) зайца на экране.

    Параметры:
    {int} surface - объект pygame.Surface
    {int} x, y - координаты центра изображения
    {int} width - ширина
    {int} height - выысота
    {tuple} color - цвет зайца

    Возвращаемые значения:
    Выводит зайца на экран
    '''
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)

    head_size = height // 4
    draw_head(surface, x, y - head_size // 2, head_size, color)

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)
    draw_eyes(surface, x - width//8 , y , width//4, height//7, height//50)
    draw_nose(surface, x, y, width//5, [255, 0, 0])
    draw_mouth(surface, x, y - height//10, width//5, height//15)


draw_hare(screen, 200, 200, 100, 300, [204, 123, 14])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()