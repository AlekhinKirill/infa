import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_mouth(surface, x, y, width, height):
    '''
    Функция рисует рот зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина рта
        height (int): Высота рта

    Возвращаемые значения:
        Pigame.Rect: Выводит рот зайца на объет surface
    '''
    pi = 3.14
    arc(surface, [0, 0, 0], (x, y, width, height), pi, 7*pi/4, 3)
    arc(surface, [0, 0, 0], (x - width, y, width, height), 5*pi/4, 2*pi,3)

def draw_nose(surface, x, y, width, color_nose):
    '''
    Функция рисует нос зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина носа
        height (int): Высота носа
        color_nose (tuple): Цвет носа в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит нос зайца на объет surface
    '''
     polygon(screen, color_nose, [(x, y - width), (x - width//2 ,y - 3*width//2), (x + width//2 ,y - 3*width//2)])

def draw_body(surface, x, y, width, height, color):
    '''
    Функция рисует туловище зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина туловища
        height (int): Высота туловища
        color (tuple): Цвет туловища в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит туловище зайца на объет surface
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    ellipse(surface, [255, 255, 255], (x - width // 3, y - height // 3, 2*width//3, 2*height//3))


def draw_head(surface, x, y, size, color):
    '''
    Функция рисует голову зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        size (int): радиус головы
        color (tuple): Цвет головы в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит голову зайца на объет surface
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Функция рисует уши зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина ушей
        height (int): Высота ушей
        color (tuple): Цвет ушей в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит уши зайца на объет surface
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Функция рисует лапы зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Длина лапы
        height (int): Ширина лапы 
        color (tuple): Цвет лап в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит лапы зайца на объет surface
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_eyes (surface, x, y, width, height, size):
    '''
    Функция рисует глаза зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина глаз
        height (int): Высота глаз
        size (int): Размер зрачка

    Возвращаемые значения:
        Pigame.Rect: Выводит глаза зайца на объет surface
    '''
    ellipse(surface, [255, 255, 255], (x - width//2, y - 4*height//3, width, height))
    ellipse(surface, [255, 255, 255], (x + width//2, y - 4*height//3, width, height))
    circle(surface, [0, 0, 0], (x + width, y - height), size)
    circle(surface, [0, 0, 0], (x, y - height), size)


def draw_hare(surface, x, y, width, height, color):
    '''
    Функция рисует (собирает) зайца.

    Параметры:
        surface (pygame.Surface): объект на котором происходит отрисовка
        x (int): Абсцисса центра изображения
        y (int): Ордината центра изображения
        width (int): Ширина зайца
        height (int): Высота зайца
        color (tuple): Основной цвет в формате RGB

    Возвращаемые значения:
        Pigame.Rect: Выводит зайца на объет surface
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
