import pygame
import sys
from template import *
from functions import *

def main():
    screen=intialize_display()
    cell=initcell()
    color=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if 800 <= x <= 1175:
                    if 25 <= y <= 115:
                        cell=autocell(screen, cell, color)
                    elif 245 <= y <= 335:
                        screen=intialize_display()
                        cell=initcell()
                    elif 355 <= y <= 445:
                        cell=growcell(cell)
                        screen=drawcell(screen, cell, color)
                    elif 465 <= y <= 555:
                        color=changecolor(color)
                        screen=drawcell(screen, cell, color)
                    elif 575 <= y <= 665:
                        screen=template_menu(screen)
                        cell=loadcell()
                        screen=intialize_menu(screen)
                        screen=drawcell(screen, cell, color)
                    elif 685 <= y <= 775:
                        pygame.quit()
                        sys.exit()
                elif 25 <= x <= 775 and 25 <= y <=775:
                    cell[(x-25)//cellscale][(y-25)//cellscale]=not cell[(x-25)//cellscale][(y-25)//cellscale]
                    screen=drawcell(screen, cell, color)

if __name__=="__main__":
    main()