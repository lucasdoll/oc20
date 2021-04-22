"""Move an image with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 800, 800

screen = pygame.display.set_mode((w, h))
running = True
background = GRAY

img = pygame.image.load('bird.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            
        elif event.type == KEYDOWN:
            if event.key in key_dict:
                background = ke_dict[event.key]
    
    screen.fill(background)
    pygame.draw.rect(screen, RED, rect)
    screen.blit(img, rect)
    pygame.display.update()

pygame.quit()
