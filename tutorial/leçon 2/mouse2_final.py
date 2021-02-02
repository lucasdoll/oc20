"""Place a rectangle with the mouse."""


# 1)ajouter un KEYDOWN event rgby pour changer la couleur
# 2)ajouter un KEYDOWN event (0-9) pour changer l'epaisseur du rectangle 

import pygame
from pygame.locals import *

RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)


key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

key_dict2 = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4,
    K_5:5, K_6:6, K_7:7, K_8:8}

#if width of the rectangle = 0, it fills up the rectangle with the color

pygame.init()
screen = pygame.display.set_mode((640, 240))


start = (0, 0)
size = (0, 0)
drawing = False
running = True
width = 1


color = GREEN

while running:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
           
        #Change the color of the rectangle with keys RGBYMK etc..
        elif event.type == KEYDOWN:
            if event.key in key_dict:
                color = key_dict[event.key]
            #change the width of the rectangle with keys 0-8. REMINDER: if width = 0, it fills it up w/ color.
            
            elif event.key in key_dict2:
                width = key_dict2[event.key]
                
    

    screen.fill(GRAY)
#     variables color and width change the color and width of the above-commented pieces of code and links them to rectangle
    pygame.draw.rect(screen, color, (start, size), width)
    pygame.display.update()

pygame.quit()