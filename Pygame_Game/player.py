import pygame
from projectile import *
from soundmanager import *
# create the class player
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        #call the super class : sprite
        super().__init__()
        self.game = game
        #caracterize the player
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        # attribut pour lancer plusieurs projectile
        self.all_projectiles = pygame.sprite.Group()
        #load image
        self.image = pygame.image.load('img/spaceship/spaceship-removebg-preview.png')
        # the images' surface
        self.rect = self.image.get_rect()
        #default position
        self.rect.x = 250
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()



    def update_health_bar(self, surface):
        if not self.health < 1:
            # définir une couleur pour notre jauge de vie
            bar_color = (111, 210, 46)
            back_bar_color = (60,63,60)
            #définir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
            bar_position = [self.rect.x + 95 , self.rect.y + 190, self.health, 5]
            # définir la position de l'arrière plan de la barre de vie
            back_bar_position = [self.rect.x + 95, self.rect.y + 190, self.max_health, 5]

            #dessiner la barre de vie
            pygame.draw.rect(surface, back_bar_color, back_bar_position)
            pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.playsound('lazer')

    # method define the moving
    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_forward(self):
        # si le joeur n'est pas en collision avec un astéroide
        if not self.game.check_collision(self, self.game.all_asteroides):
            self.rect.y -= self.velocity
    def move_back(self):
        self.rect.y += self.velocity
