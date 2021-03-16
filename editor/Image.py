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

    def __init__(self):
        self.img0 = None
        self.img = None
        self.rect = None
        self.file_name = None
        self.scale = 1
        self.angle = 0

    def load(self):
        file_name = input('Indiquer le chemin de votre image avec extension:')
        self.file_name = file_name

        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)
        path = os.path.join(path, file_name)

        img0 = pygame.image.load(path)
        img0.convert()
        self.img0 = img0

        self.img = img0.copy()
        self.rect = img0.get_rect()
        self.rect.center = center
