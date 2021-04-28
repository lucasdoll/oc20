import pygame
from spaceship_enemy import *
# créer une classe pour gérer cet évenement
class Bossfight:

    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 3
        self.game = game
        self.fall_mode = False

        # définir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percentage(self):
        self.percent += self.percent_speed/1

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # apparaitre des boules de feux
        for i in range(1, 2):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenemt est totalement charger
        if self.is_full_loaded() and len(self.game.all_asteroides) == 0:
            self.meteor_fall()
            self.fall_mode = True # activer la pluie de comètes



    def update_bar(self, surface):

        # ajouter du pourcentage à la bar
        self.add_percentage()

        # barre noir qui va être en arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height() - 15, # longueur de l'axe y
            surface.get_width(), # longueur de la fenêtre
            10])
        # barre rouge qui est la jauge d'évenement
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # longueur de l'axe y
            (surface.get_width()/100) * self.percent,  # longueur de la fenêtre
            10])

