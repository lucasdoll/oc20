import pygame
import random
from asteroide import*
from game import *
# créer une classe pour gérer cette comet
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # définir quelle est l'image associé
        self.image_load = pygame.image.load('img/spaceship/spaceship2-removebg-preview.png')
        self.image = pygame.transform.scale(self.image_load, (120, 120))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(-10, 500)
        self.rect.y = -80
        self.attack = 20
        self.comet_event = comet_event
        self.direction = random.randint(0, 1)
        self.health = 100
        self.max_health = 100

    def update_health_bar_comet(self, surface):
        # définir une couleur pour notre jauge de vie
        bar_color = (111, 210, 46)
        back_bar_color = (60,63,60)
        #définir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
        bar_position = [self.rect.x , self.rect.y - 10, self.health, 5]
        # définir la position de l'arrière plan de la barre de vie
        back_bar_position = [self.rect.x, self.rect.y - 10, self.max_health, 5]

        #dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def remove(self):
        self.comet_event.all_comets.remove(self)

        # vérifier si le nombre de cometes est de zéro
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre a 0
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_asteroide(Big_Asteroide)
            self.comet_event.game.spawn_asteroide(Big_Asteroide)
            self.comet_event.game.spawn_asteroide(Med_Asteroide)
            self.comet_event.game.spawn_asteroide(Med_Asteroide)
            self.comet_event.game.spawn_asteroide(Small_Asteroide)


    def move_spaceship(self):

        self.rect.y += self.velocity
        if self.rect.y == - 20:
            if self.direction == 1:
                self.rect.x += self.velocity
                if self.rect.x >= 0:
                    self.rect.x -= self.velocity
                if self.rect.x <= -200:
                    self.rect.x += self.velocity

            if self.direction == 0:
                self.rect.x -= self.velocity
                if self.rect.x >= 0:
                    self.rect.x -= self.velocity
                if self.rect.x <= -200:

                    self.rect.x += self.velocity


    def fall(self):
        self.rect.y += self.velocity

        # le déplacement ne se fait que s'il n'y a pas de collision
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):

            # retirer la boule de feux
            self.remove()
            # subir 20 points de dégat
            self.comet_event.game.player.damage(self.attack)

        # si l'astéroide à traversé l'écran
        if self.rect.y >= 810:
            self.remove()
            self.rect.x = random.randint(-10, 500)
            self.rect.y = -15
            self.velocity = random.randint(1, 2)

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:

                # remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


