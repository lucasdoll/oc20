
import pygame
from player import *
from asteroide import *
from Bossfight import *
from soundmanager import *


WIDTH, HEIGHT = 800, 800
# create class Game
class Game:
    def __init__(self):
        # define if the game begun or not
        self.is_playing = False
        # generate player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'evenemt de pluie de comet
        self.comet_event = BossEvent(self)
        # définir un groupe de monstre
        self.all_asteroides = pygame.sprite.Group()
        # sound
        self.sound_manager = Soundmanager()
        # Establishing font for labels for counters
        self.main_font = pygame.font.Font('fonts/main_font.ttf', 50)
        # score
        self.score = 0
        # créer un attribut qui va enregistrer toute les touche active
        self.pressed = {}

    def addscore(self, points):
        self.score += points

    def start(self):
        self.is_playing = True
        self.spawn_asteroide(Med_Asteroide)
        self.spawn_asteroide(Med_Asteroide)
        self.spawn_asteroide(Big_Asteroide)
        self.spawn_asteroide((Small_Asteroide))
        self.spawn_asteroide((Small_Asteroide))
        self.spawn_asteroide((Small_Asteroide))


    def game_over(self):
        # remettre le jeu à neuf, retirer les monstre, remettre le joueur a 100 de vie, jeu en attente
        self.all_asteroides = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        # default position
        self.player.rect.x = 250
        self.player.rect.y = 500
        self.is_playing = False
        self.score = 0

    def update(self, screen):

        # lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        score_label = self.main_font.render(f"Score: {self.score}", 1, (255, 255, 255))

        # drawing variables
        # screen.blit(lives_label, (10, 10))
        screen.blit(score_label, (WIDTH - score_label.get_width() - 10, 10))

        # generate the players'image
        screen.blit(self.player.image, self.player.rect)

        # appliquer l'ensemble des images de mon groupes de projectiles
        self.player.all_projectiles.draw(screen)
        # actualiser la barre de bie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenemt du jeu
        self.comet_event.update_bar(screen)

        # appliquer l'ensemble desy images de mon groupe de comètes
        self.comet_event.all_comets.draw(screen)

        # récupérer les projectiles du joeur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.update_health_bar_comet(screen)
            comet.move_spaceship()

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_asteroides.draw(screen)

        # récupérer les monstres de notre jeu
        for asteroide in self.all_asteroides:
            asteroide.forward()
            asteroide.update_health_bar(screen)

        # verifie si le joueur souhaite tourner à gauche, à droite, devant, ou en arrière et aussi vérifie s'il ne dépace
        # pas lécran !!
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_a) and self.player.rect.x > -18:
            self.player.move_left()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y < 624:
            self.player.move_back()
        elif self.pressed.get(pygame.K_w) and self.player.rect.y > 0:
            self.player.move_forward()





    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # on peut remplacer la valeur False par dockil qui est que le joueur meut s'il touvhe le monstre

    def spawn_asteroide(self, asteroide_class_name):
        self.all_asteroides.add(asteroide_class_name.__call__(self)) # call permet d'instensier l'objet
