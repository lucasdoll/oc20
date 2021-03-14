import pygame
from pygame.locals import*
from Image import *
# define the shape (rectangle and ellipse)

flags = pygame.RESIZABLE
screen = pygame.display.set_mode((640, 240), flags)

# ENTRE LES GUILLEMETS EST LE TEXTE VOULU ET LA POSITIO

class Shape:
    def __init__(self, rect, color=RED, width=1):
        self.rect = rect
        self.color = color
        self.width = width

    def draw_rectangle(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)

    def draw_ellipse(self):
        pygame.draw.ellipse(screen, self.color, self.rect, self.width)
