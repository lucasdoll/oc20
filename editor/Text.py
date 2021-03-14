import pygame
from Colors import *
from Text import *

# initialize Pygame and the window
pygame.init() #initialize pygame
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((640, 240), flags)

# ENTRE LES GUILLEMETS EST LE TEXTE VOULU ET LA POSITION

# settings text:

class Text:  #creating a Text class for Text objects
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        #text parameters
        self.fontname = None
        self.fontsize = 72 #taille du texte
        self.fontcolor = BLACK
        self.set_font()
        self.render()

    # setting font parameters from established size and font desired
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def blit(self):
        #defining blit text image to screen
        screen.blit(self.img, self.rect)


    #Rendering the text with desired font into an image
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        #setting text to topleft position
