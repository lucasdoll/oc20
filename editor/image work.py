import pygame
import os
import pickle
from pygame.locals import *
import sys
import math

pygame.init() #initialize pygame
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((640, 240), flags)

# ENTRE LES GUILLEMETS EST LE TEXTE VOULU ET LA POSITION

# concernant les options d'affichage
flags = RESIZABLE
rect = Rect(0, 0, 640, 240)

bg = Color((255, 204, 203))


screen = pygame.display.set_mode(rect.size, flags)

w, h = 640, 240
module = sys.modules['__main__']
path, name = os.path.split(module.__file__)

#class Image
class Image:

    def __init__(self,image_finish, rect):
        self.image_finish = image_finish
        self.rect = rect

    def pos_image(self):
        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)


        path = os.path.join(path, image)

        img0 = pygame.image.load(path)
        img0.convert()

        rect0 = img0.get_rect()

        center = w // 2, h // 2
        img = img0
        rect = img.get_rect()
        rect.center = center
        screen.blit(img, rect)

def pos_draw2(image):
    module = sys.modules['__main__']
    path, name = os.path.split(module.__file__)
    path = os.path.join(path, image)

    img0 = pygame.image.load(path)
    img0.convert()

    rect0 = img0.get_rect()

    img = img0
    rect = img.get_rect()
    rect.center = center
    screen.blit(img, rect)


# settings for loading the image
center = w // 2, h // 2
Image_list = []
#settings before the draw
angle = 0
scale = 1

moving = False
movement = False
rotation = False
mouse = pygame.mouse.get_pos()


while running:

    screen.fill(bg)  # window color
