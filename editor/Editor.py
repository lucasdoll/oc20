import pygame
import os
import pickle
from pygame.locals import *
import sys
import math
# audio and music
from pygame import mixer
from Shapes import*
from Text import*
from Colors import *

clock = pygame.time.Clock()

# initializing mixer for audio and music
mixer.init()

pygame.display.set_caption('Graphic Editor') #Naming the window


def play_music():
    mixer.music.load('gameaudio.mp3')
    mixer.music.play()


bg = Color((255, 204, 203))
mbg = pygame.image.load('sky.jpg')


# initialize Pygame and the window
pygame.init() #initialize pygame
flags = RESIZABLE
screen = pygame.display.set_mode((640, 240), flags)
text = Text('Graphic Editor', pos=(30, 30)) # Text variable for whatever is wanted on screen
# ENTRE LES GUILLEMETS EST LE TEXTE VOULU ET LA POSITION

# concernant les options d'affichage
flags = RESIZABLE
rect = Rect(0, 0, 640, 240)


running = True


# initialize Pygame and the window
pygame.init() #initialize pygame

#Titre et icone
pygame.display.set_caption("Editeur Pygame")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

# executing shortcuts function
 # Find the the key/mod combination in the dictionary and execute the cmd.

play_music()


# ALL LISTS
Text_list = []
# list for save the rectangles and ellipses created
Rectangle = []
Ellipse = []

# Polygon's points
points = []

# all settings for the creation of rectangles, ellipses and polygon
start = (0, 0)
size = (0, 0)
drawing = False
color = RED
width = 1

w, h = 640, 240
module = sys.modules['__main__']
path, name = os.path.split(module.__file__)



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
image_config = None

#settings before the draw
angle = 0
scale = 1

moving = False
movement = False
rotation = False
mouse = pygame.mouse.get_pos()

        # initialize the first shape (default: Rectangle)
shapes = Rectangle

#list background
background = []


# search if they have a save
if os.path.exists('sauvegarde_dessin') is True:
    # search if rectangle's save exists
    if os.path.exists('sauvegarde_dessin/rectangle.pkl') is True:
        # open the file
        with open('sauvegarde_dessin/rectangle.pkl','rb') as rectangle_save:
            Rectangle = pickle.load(rectangle_save)
    # same procedure
    if os.path.exists('sauvegarde_dessin/ellipse.pkl') is True:
        with open('sauvegarde_dessin/ellipse.pkl', 'rb') as ellipse_save:
            Ellipse = pickle.load(ellipse_save)
    # same procedure
    if os.path.exists('sauvegarde_dessin/polygon.pkl') is True:
        with open('sauvegarde_dessin/polygon.pkl', 'rb') as polygon_save:
            points = pickle.load(polygon_save)
    if os.path.exists('sauvegarde_dessin/background.pkl') is True:
        with open('sauvegarde_dessin/background.pkl', 'rb') as backrgound_save:
            background = pickle.load(backrgound_save)
            bg = background.pop()


# initialize menu
menu = False
while running:


    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False

        screen.fill((181, 6, 5))
        clock.tick(30)
        screen.blit(mbg, (0, 0))

        pygame.display.update()


    screen.fill(bg)  # window color
    text.blit()  # blitting text to Screen

    for event in pygame.event.get():
        if event.type == QUIT:
            if event.type == QUIT:
                background.append(bg)
                question = input('Voulez-vous faire une sauvegarde de votre dessin?(oui/non)')
                if question == 'oui':
                    if os.path.exists('sauvegarde_dessin') is False:
                        os.mkdir('sauvegarde_dessin')
                    with open('sauvegarde_dessin/rectangle.pkl', 'wb') as rectangle_file:
                        pickle.dump(Rectangle, rectangle_file)
                    with open('sauvegarde_dessin/ellipse.pkl', 'wb') as ellipse_file:
                        pickle.dump(Ellipse, ellipse_file)
                    with open('sauvegarde_dessin/polygon.pkl', 'wb') as polygon_file:
                        pickle.dump(points, polygon_file)
                    with open('sauvegarde_dessin/background.pkl', 'wb') as background_file:
                        pickle.dump(background, background_file)

            running = False
        if event.type == KEYDOWN:

            # launch menu
            if event.key == K_m:
                menu = True
                shapes = None
            # import text
            if event.key == K_t:
                texte_input = input('Veuillez insérer du texte:')
                texte_pos_x = int(input('Vueillez donner la première cordonnée x:'))
                texte_pos_y = int(input('Veuillez donner la seconde cordonnée y: '))
                text_objet = Text(texte_input, pos=(texte_pos_x, texte_pos_y))
                Text_list.append(text_objet)
                shapes = 'text_delete'
            # move image
            if event.key == K_d:
                movement = True
                rotation = False
                shapes = 'image_delete'

            # can stop the images' movement
            elif event.key == K_s:
                movement = False


            # import image
            elif event.key == K_i:
                image = Image()
                image.load()
                Image_list.append(image)
                print(Image_list)
                shapes = 'image_delete'
                image_config = True


            # can rotate the image
            if image_config is True:
                image_rot = Image_list[-1]

                #change angle
                if event.key == K_y:
                    image.angle += 10
                    image_rot.img = pygame.transform.rotozoom(image_rot.img0, image_rot.angle, image_rot.scale)
                    shapes = 'image_delete'

                elif event.key == K_h :
                    image.angle -= 10
                    shapes = 'image_delete'
                    image_rot.img = pygame.transform.rotozoom(image_rot.img0, image_rot.angle, image_rot.scale)

                #rotation 1.1
                elif event.key == K_p:
                    image.scale /= 1.1
                    image_rot.img = pygame.transform.rotozoom(image_rot.img0, image_rot.angle, image_rot.scale)
                    shapes = 'image_delete'

                elif event.key == K_z:
                    image.scale *= 1.1
                    image_rot.img = pygame.transform.rotozoom(image_rot.img0, image_rot.angle, image_rot.scale)
                    shapes = 'image_delete'
                # turn image
                elif event.key == K_f and event.mod & KMOD_ALT:
                    image_rot.img = pygame.transform.flip(image_rot.img, True, False)
                    shapes = 'image_delete'

                # flip image
                elif event.key == K_f:
                    image_rot.img = pygame.transform.flip(image_rot.img, False, True)
                    shapes = 'image_delete'

            if event.key == K_b:
                bg = BLUE
            if event.key == K_x:
                bg = GOLD
            if event.key == K_c:
                bg = CYAN
            if event.key == K_v:
                bg = MAGENTA
            if event.key == K_w:
                bg = WHITE
            if event.key == K_n:
                bg = BLACK
            # create Rectangle
            if event.key == K_r:
                shapes = Rectangle
            # create Ellipse
            if event.key == K_e:
                shapes = Ellipse
            # create polygon
            if event.key ==  K_l:
                shapes = points


            elif event.key == K_ESCAPE:
                # delete polygon's point
                if shapes == points:
                    if len(points) > 0:
                        points.pop()
                # delete rectangle
                elif shapes == Rectangle:
                    Rectangle.pop()
                elif shapes == Ellipse:
                    Ellipse.pop()
                # delete Image
                elif shapes == 'image_delete':
                    Image_list.pop()
                    image_config = False
                # delete Text
                elif shapes == 'text_delete':
                    Text_list.pop()

            # widths' setting
            if event.key == K_0:
                width = 0
            if event.key == K_1:
                width = 1
            if event.key == K_2:
                width = 3
            # colors' setting
            if event.key == K_7:
                color = RED
            if event.key == K_g :
                color = GREEN
            if event.key == K_8:
                color = BLUE


        elif event.type == MOUSEBUTTONDOWN:
            if movement == True:
                if rect.collidepoint(event.pos):
                    moving = True
                # create rectangle
            if shapes == Rectangle:
                start = event.pos
                s = Shape(Rect(start, (0, 0)), color, width)
                shapes.append(s)
                drawing = True
                # create Ellipse
            elif shapes == Ellipse:
                start = event.pos
                s = Shape(Rect(start, (0, 0)), color, width)
                shapes.append(s)
                drawing = True
                # create point's polygon
            elif shapes == points:
                points.append(event.pos)
                drawing = True



        # stop drawing
        elif event.type == MOUSEBUTTONUP:
            drawing = False
            if movement == True:
                moving = False


        elif event.type == MOUSEMOTION and drawing:
                # training the rectangle
            if shapes == Rectangle:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                shapes[-1].rect.size = size
                # training the ellipse
            elif shapes == Ellipse:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                shapes[-1].rect.size = size
                # training the point's polygon
            elif shapes == points:
                    points[-1] = event.pos

        # move the image to the position of the mouse
        if event.type == MOUSEMOTION and moving is True:
            image.rect.move_ip(event.rel)
            pygame.draw.rect(screen, GREEN, image.rect, 1)




        # draw all shapes in the screen and keep in the screen
        for rectangle in Rectangle:
            rectangle.draw_rectangle()
        for ellipse in Ellipse:
            ellipse.draw_ellipse()
        if len(points) > 1:
            line = pygame.draw.lines(screen, RED, True, points, width)

        for text in Text_list:
            text.render()
            text.blit()

        for image in Image_list:
            screen.blit(image.img, image.rect)



        pygame.display.update()  # updating Pygame after blit

pygame.quit()
