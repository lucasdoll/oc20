import pygame
from Colors import *
import os
import sys

# settings for loading the image
w, h = 640, 240
module = sys.modules['__main__']
path, name = os.path.split(module.__file__)
center = w // 2, h // 2
Image_list = []

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
