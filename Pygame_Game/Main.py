import pygame
from pygame.locals import *
import math
from game import *
from pygame import mixer
'''Ce fichier est pour l'ensemble du code'''

'''sprites est une super classe qui permet à l'objet de se déplacer '''

#initialisation de la page du jeu
pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 160


# load music and play
mixer.music.load('music/music.mp3')
mixer.music.play(-1)

# initialisations de la page
pygame.display.set_caption('shooter Game')
screen = pygame.display.set_mode((800, 800))

# import the background
background = pygame.image.load('img/backrgound/background.jpg')

# importer charger notre boutton play
play_button = pygame.image.load('img/Menu/banner_start.png')
play_button = pygame.transform.scale(play_button, (300, 300))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_width() / 3)
# math.ceil permet de rendre un nombre virgule --> un nombre eniter


# charge Game
game = Game()
#charge player
player = Player(game)

running = True

# boucle tant que cette condition est vrai
while running:

    #generate the background
    screen.blit(background, (0,0))

    #vérifier si notre jeu a commencé ou non
    if game.is_playing is True:
        # declencher les instructions de la partie
        game.update(screen)

    # vérifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenu
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    # update the screen
    pygame.display.flip()


    for event in pygame.event.get():
        # exit game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')
        # detect if player touches a key
        elif event.type == pygame.KEYDOWN:
            # permet que lorsqu'on appuie sur une touche il rentre dans un dictionnaire et
            # premet de vérifier si oui ou non elle est active
            game.pressed[event.key] = True

            #detecter si la touche espace est détecter pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                # adding sound to the firing projectile
                bullet_sound = mixer.Sound('music/lazer.mp3')
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    pass


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si la souris est sur le boutton de lancement
            if play_button_rect.collidepoint(event.pos):
                # démarer la partie
                game.start()
                game.sound_manager.playsound('click')


    # fixer le nombre de fps sur le jeu
    clock.tick(FPS)



