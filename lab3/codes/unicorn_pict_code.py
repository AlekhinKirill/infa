import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

c1 = (244, 148, 205) 
c2 = (202, 123, 223)
c3 = (157, 141, 207)


def e(c, x, m):
    '''
    Function for drawing scalable ellipses
    Arguments:
    c - color in the format (r, g, b)
    x = (x0, y0, N), where x0, y0 is the point relative to which the scale is changed; N - reduction factor
    m = (x1, y1, l1, l2), where x1, y1 are the coordinates of the ellipse relative to the point x0, y0; l1, l2 - the lengths of the sides of the rectangle in which the ellipse is inscribed
    '''
    global screen
    N = x[2]
    k = 1
    d = 0
    if N < 0:
        k = -1
        N = -N
        d = -m[2]//N
    ellipse(screen, c, (x[0] + d+ k*m[0]//N, x[1] + m[1]//N, m[2]//N, m[3]//N))


def r(c, x, m):
    '''
    Function for drawing scalable rectangles
    Arguments:
    c - color in the format (r, g, b)
    x = (x0, y0, N), where x0, y0 is the point relative to which the scale is changed; N - reduction factor
    m = (x1, y1, l1, l2), where x1, y1 are the coordinates of the rectangle relative to the point x0, y0; l1, l2 - the lengths of the sides of the rectangle 
    '''
    global screen
    N = x[2]
    k = 1
    d = 0
    if N < 0:
        k = -1
        N = -N
        d = -m[2]//N
    rect(screen, c, (x[0] + d+ k*m[0]//N, x[1] + m[1]//N, m[2]//N, m[3]//N))
    
        
def unicorn_right(x, y, N, color):
    '''
    Function for drawing a unicorn pointing to the right
    Arguments:
    x, y - coordinates of the upper left point of the unicorn
    N - reduction factor
    color - color in the format (r, g, b)
    '''
    X = (x, y, N)
    k = 1
    if N < 0:
      k = -1
      N = -N
    e(color, X, (0, 0, 150, 60))
    r(color, X, (115, -40, 30, 60))
    circle(screen, color, (x + k*140//N, y - 40//N), 15//N)
    e(color, X, (140, -45, 30, 15))
    e(c1, X, (110, -60, 30, 15))
    e(c1, X, (100, -50, 30, 15))
    e(c1, X, (90, -40, 40, 15))
    e(c1, X, (100, -20, 30, 10))
    e(c2, X, (80, -20, 40, 10))
    e(c1, X, (85, -30, 35, 10))
    e(c1, X, (70, -7, 40, 10))
    e(c3, X, (92, -25, 40, 10))
    e(c1, X, (90, -10, 40, 15))
    e(c3, X, (80, -15, 40, 10))
    e(c3, X, (83, 0, 40, 10))
    e(c3, X, (107, -43, 27, 10))
    e(c2, X, (95, -35, 20, 7))
    e(c1, X, (10, 0, 30, 15))
    e(c1, X, (0, 10, 30, 15))
    e(c1, X, (-10, 20, 40, 15))
    e(c1, X, (0, 40, 30, 10))
    e(c2, X, (-20, 40, 40, 10))
    e(c1, X, (-15, 30, 35, 10))
    e(c1, X, (-30, 53, 40, 10))
    e(c3, X, (-8, 35, 40, 10))
    e(c1, X, (-10, 50, 40, 15))
    e(c3, X, (-20, 45, 40, 10))
    e(c3, X, (-17, 60, 40, 10))
    e(c3, X, (7, 17, 27, 10))
    e(c2, X, (-5, 25, 20, 7))
    r(color, X, (105, 20, 10, 70))
    r(color, X, (130, 40, 10, 70))
    r(color, X, (35, 20, 10, 70))
    r(color, X, (60, 40, 10, 70))
    circle(screen, c1, (x + k*142//N, y - 42//N), 7//N)
    e((255, 255, 255), X, (138, -42, 9, 2))
    circle(screen, (0, 0, 0), (x + k*147//N, y - 42//N), 3//N)
    polygon(screen, c3 , [[x + k*132//N, y - 55//N], [x + k*140//N, y - 55//N], [x + k*145//N, y - 90//N]])


def unicorn_left(x, y, N, color):
    '''
    Function for drawing a unicorn pointing to the left
    Arguments:
    x, y - coordinates of the upper left point of the unicorn
    N - reduction factor
    color - color in the format (r, g, b)
    '''
    unicorn_right(x + 150//N, y, -N, color)

def tree(color_leaves, color_apples, color_trunk, x, y, N):
    '''
    Function for drawing a tree
    Arguments:
    x, y - coordinates of the upper left point of the unicorn
    N - reduction factor
    color - color in the format (r, g, b)
    '''
    X = (x, y, N)
    rect(screen, color_trunk, (x, y, 30//N, 100//N))
    e(color_leaves, X, (-85, -150, 200, 100))
    e(color_leaves, X, (-45, -230, 120, 150))
    e(color_leaves, X, (-45, -80, 120, 100))
    circle(screen, color_apples, (x + 5//N, y - 180//N), 15//N)
    circle(screen, color_apples, (x + 50//N, y - 20//N), 15//N)
    circle(screen, color_apples, (x + 75//N, y - 90//N), 15//N)
    circle(screen, color_apples, (x - 45//N, y - 100//N), 15//N)

rect(screen, (9, 247, 207), (0, 0, 500, 500))
rect(screen, (19, 248, 8), (0, 170, 500, 400))
circle(screen, (225, 225, 0), (470, 40), 80)
circle(screen, (240, 170, 0), (470, 40), 60)
tree((64, 109, 33), (244, 249, 23), (111, 23, 23), 30, 150, 3 )
tree((101, 170, 37), (255, 0, 0), (137, 109, 71), 190, 180, 3 )
tree((5, 70, 2), (244, 148, 205), (255, 255, 255), 95, 350, 1 )
unicorn_right(300, 370, 1, (170, 50, 80))
unicorn_left(220, 300, 2, (231, 246, 33))
unicorn_right(330, 250, 2, (170, 250, 250))
unicorn_right(260, 200, 3, (255, 255, 255))
unicorn_left(440, 200, 3, (181, 51, 233))
line(screen, (225, 225, 0), [370, 60], [330, 70], 7)
line(screen, (225, 225, 0), [370, 30], [325, 33], 7)
line(screen, (225, 225, 0), [375, 90], [345, 110], 7)
line(screen, (225, 225, 0), [400, 110], [370, 140], 7)
line(screen, (225, 225, 0), [420, 135], [400, 160], 7)
line(screen, (225, 225, 0), [450, 140], [440, 170], 7)

pygame.display.update()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
