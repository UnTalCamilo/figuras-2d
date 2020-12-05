
from library.figures.circle import *
from library.figures.graphic import *
from library.figures.polygon import *
from library.figures.equilateral_t import *
from library.figures.right_t import *
from library.figures.rectangle import *
from library.figures.square import *
from library.figures.cube import *
import pygame
from pygame.locals import *
import sys


SCREEN_WIDTH = 600 # x
SCREEN_HEIGHT = 600 # y

DRAWEVENT = USEREVENT + 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128,0,128)
AQUA = (0, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.time.set_timer(DRAWEVENT, 100)
def main():
    pygame.init()
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("pixel")

    window = Graph(screen)
    
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                
                
                #plano(window)
                
                
                c = Circle(400,150,100)
                window.style(7, YELLOW)
                c.draw(window)

                ip = IrregularP([50,200,150,20,200,170,240,0,300,300],5)
                window.style(5, GREEN)
                ip.draw(window)
                
                window.style(4, BLUE)
                rp = RegularP(300,500,100,6)
                rp.draw(window)
                
                window.style(6, RED)
                et = RightT(450,500,100, 200)
                et.draw(window)

                window.style(0, WHITE)
                sx = Cube(110,350,100)
                sx.draw(window)
                print("**", pygame.mouse.get_pos())
                
            elif event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h),
                                                pygame.RESIZABLE)
        pygame.display.flip()

        



def middle_point(screen):
    x = round((screen.get_width()) / 2)
    y = round((screen.get_height()) / 2)

    return (x, y)


def plano(g):
    
    center = middle_point(screen)
    space = 0.4
    module = 30
    if g.screen.get_width() > g.screen.get_height(): size = round(space * g.screen.get_width())
    else: size = round(space * g.screen.get_height())

    g.line(center[0] - size, center[1] , center[0] + size, center[1])
    g.line(center[0], center[1] - size , center[0], center[1] + size)
    
    rect_x = []
    rect_y = []
    rect_2x = []
    rect_2y = []

    
    for i in range(1, size):
        if i % module == 0:
            rect_x.append((center[0] - i, center[1]))
            rect_2x.append((center[0] + i, center[1]))
            rect_y.append((center[0], center[1] - i))
            rect_2y.append((center[0], center[1] + i))

    rectas(g, rect_x, rect_2x, rect_y, rect_2y, center)



def rectas(g, rect_x, rect_2x, rect_y, rect_2y, center):
    g.draw_lines(rect_x, rect_y[::-1])
    g.draw_lines(rect_y, rect_2x[::-1])
    g.draw_lines(rect_x, rect_2y[::-1])
    g.draw_lines(rect_2x, rect_2y[::-1])
        
def reliquias(screen):
    center = middle_point(screen)

if __name__ == "__main__":
    main()