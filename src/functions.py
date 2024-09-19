import pygame
import sys
import time
from template import *

def intialize_display():
    pygame.init()
    screen = pygame.display.set_mode(field)
    pygame.display.set_caption("LifeGame")
    screen.fill(fieldcolor)
    pygame.draw.rect(screen, cellcolor, (25, 25, 750, 750))
    screen = intialize_menu(screen)
    pygame.display.flip()
    return screen

def intialize_menu(screen):
    font = pygame.font.SysFont("msgothic", 50)
    messages=["Start", "Stop", "Reset", "Next", "Color", "Load", "Quit"]
    for i in range(7):
        pygame.draw.rect(screen, buttoncolor, (800, 25+110*i, 175, 90))
        text=font.render(messages[i], True, fontcolor)
        screen.blit(text, (820, 45+110*i))
    return screen

def template_menu(screen):
    font = pygame.font.SysFont("msgothic", 50)
    messages=["", "", "", "", "", "", ""]
    for i in range(7):
        pygame.draw.rect(screen, buttoncolor, (800, 25+110*i, 175, 90))
        text=font.render(messages[i], True, fontcolor)
        screen.blit(text, (820, 45+110*i))
    pygame.display.flip()
    return screen

def changecolor(color):
    return (color+1)%len(lifecolor)

def initcell():
    return [[False]*cellrange for _ in range(cellrange)]

def drawcell(screen,cell,color):
    for i in range(cellrange):
        for j in range(cellrange):
            if cell[i][j]:
                pygame.draw.rect(screen, lifecolor[color], (25+cellscale*i, 25+cellscale*j, cellscale, cellscale))
            else:
                pygame.draw.rect(screen, cellcolor, (25+cellscale*i, 25+cellscale*j, cellscale, cellscale))
    pygame.display.flip()
    return screen

def growcell(cell):
    buf=cell.copy()
    cell=[[False]*cellrange for _ in range(cellrange)]
    count=0
    if buf[0][1]:
        count+=1
    if buf[1][0]:
        count+=1
    if buf[1][1]:
        count+=1
    if cell[0][0]:
        if count==2 or count==3:
            cell[0][0]=True
        else:
            cell[0][0]=False
    else:
        if count==3:
            cell[0][0]=True
        else:
            cell[0][0]=False
    count=0
    if buf[0][cellrange-2]:
        count+=1
    if buf[1][cellrange-1]:
        count+=1
    if buf[1][cellrange-2]:
        count+=1
    if cell[0][cellrange-1]:
        if count==2 or count==3:
            cell[0][cellrange-1]=True
        else:
            cell[0][cellrange-1]=False
    else:
        if count==3:
            cell[0][cellrange-1]=True
        else:
            cell[0][cellrange-1]=False
    count=0
    if buf[cellrange-2][0]:
        count+=1
    if buf[cellrange-1][1]:
        count+=1
    if buf[cellrange-2][1]:
        count+=1
    if cell[cellrange-1][0]:
        if count==2 or count==3:
            cell[cellrange-1][0]=True
        else:
            cell[cellrange-1][0]=False
    else:
        if count==3:
            cell[cellrange-1][0]=True
        else:
            cell[cellrange-1][0]=False
    count=0
    if buf[cellrange-2][cellrange-1]:
        count+=1
    if buf[cellrange-1][cellrange-2]:
        count+=1
    if buf[cellrange-2][cellrange-2]:
        count+=1
    if cell[cellrange-1][cellrange-1]:
        if count==2 or count==3:
            cell[cellrange-1][cellrange-1]=True
        else:
            cell[cellrange-1][cellrange-1]=False
    else:
        if count==3:
            cell[cellrange-1][cellrange-1]=True
        else:
            cell[cellrange-1][cellrange-1]=False
    for i in range(1, cellrange-1):
        count=0
        if buf[i-1][0]:
            count+=1
        if buf[i-1][1]:
            count+=1
        if buf[i][1]:
            count+=1
        if buf[i+1][1]:
            count+=1
        if buf[i+1][0]:
            count+=1
        if cell[i][0]:
            if count==2 or count==3:
                cell[i][0]=True
            else:
                cell[i][0]=False
        else:
            if count==3:
                cell[i][0]=True
            else:
                cell[i][0]=False
    for i in range(1, cellrange-1):
        count=0
        if buf[i-1][cellrange-1]:
            count+=1
        if buf[i-1][cellrange-2]:
            count+=1
        if buf[i][cellrange-2]:
            count+=1
        if buf[i+1][cellrange-2]:
            count+=1
        if buf[i+1][cellrange-1]:
            count+=1
        if cell[i][cellrange-1]:
            if count==2 or count==3:
                cell[i][cellrange-1]=True
            else:
                cell[i][cellrange-1]=False
        else:
            if count==3:
                cell[i][cellrange-1]=True
            else:
                cell[i][cellrange-1]=False
    for j in range(1, cellrange-1):
        count=0
        if buf[0][j-1]:
            count+=1
        if buf[1][j-1]:
            count+=1
        if buf[1][j]:
            count+=1
        if buf[1][j+1]:
            count+=1
        if buf[0][j+1]:
            count+=1
        if cell[0][j]:
            if count==2 or count==3:
                cell[0][j]=True
            else:
                cell[0][j]=False
        else:
            if count==3:
                cell[0][j]=True
            else:
                cell[0][j]=False
    for j in range(1, cellrange-1):
        count=0
        if buf[cellrange-1][j-1]:
            count+=1
        if buf[cellrange-2][j-1]:
            count+=1
        if buf[cellrange-2][j]:
            count+=1
        if buf[cellrange-2][j+1]:
            count+=1
        if buf[cellrange-1][j+1]:
            count+=1
        if cell[cellrange-1][j]:
            if count==2 or count==3:
                cell[cellrange-1][j]=True
            else:
                cell[cellrange-1][j]=False
        else:
            if count==3:
                cell[cellrange-1][j]=True
            else:
                cell[cellrange-1][j]=False
    for i in range(1, cellrange-1):
        for j in range(1, cellrange-1):
            count=0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if buf[i+x][j+y]:
                        count+=1
            if buf[i][j]:
                count-=1
                if count==2 or count==3:
                    cell[i][j]=True
                else:
                    cell[i][j]=False
            else:
                if count==3:
                    cell[i][j]=True
                else:
                    cell[i][j]=False
    return cell

def autocell(screen, cell,color):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if 800 <= x <= 1175:
                    if 135 <= y <= 225:
                        return cell
        cell=growcell(cell)
        screen=drawcell(screen, cell,color)
        time.sleep(0.5)

def loadcell():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if 800 <= x <= 1175:
                    if 25 <= y <= 115:
                        return cells[0]
                    elif 135 <= y <= 225:
                        return cells[1]
                    elif 245 <= y <= 335:
                        return cells[2]
                    elif 355 <= y <= 445:
                        return cells[3]
                    elif 465 <= y <= 555:
                        return cells[4]
                    elif 575 <= y <= 665:
                        return cells[5]
                    elif 685 <= y <= 775:
                        return cells[6]