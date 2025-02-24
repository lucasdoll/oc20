import pygame
from pygame.locals import *

# Tools > Install packages...
# Find pygame
# Install

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

background = GRAY

key_dict = {K_k:BLACK, K_w:WHITE,
            K_r:RED, K_g:GREEN, K_b:BLUE,
            K_y:YELLOW, K_c:CYAN, K_m:MAGENTA}

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill(background)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == KEYDOWN:
            print(event)
            if event.key in key_dict:
                background = key_dict[event.key]
                
            screen.fill(background)
            pygame.display.update()

pygame.quit()

# import pygame
# from pygame.locals import *
# pygame.display.init()
# 
# MAGENTA = (255, 0, 255)
# BLACK = (0, 0, 0)
# GRAY = (127, 127, 127)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)
# 
# screen = pygame.display.set_mode((640, 480)) 
# screen.fill(MAGENTA)
# 
# key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
#     K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}
# 
# print(key_dict)
# 
# image = pygame.image.load("L183715_Reseau/Mario.jpeg") 
# pygame.display.flip()
# loop = True
# while loop: 
#     for event in pygame.event.get():
#         if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
#             loop = False
# 
# pygame.quit()
