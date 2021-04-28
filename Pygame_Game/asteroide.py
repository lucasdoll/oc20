import pygame
import random



# définir la classe qui va gérer les monstres présent dans le jeu
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, game, image, score_value):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-10, 500)
        self.rect.y = -15
        self.origin_image = self.image
        self.angle = 0
        self.score_value = score_value

    def rotation(self):
        # tourner l'asteroide
        self.angle += 0.2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def set_score_value(self, amount):
        self.score_value = amount

    def damage(self, amount):
        #  Infliger des dégats
        self.health -= amount

        #vérifier si son nombre de points de vie est inférieur ou égale à zéro

        if self.health <= 0:
            # supprimer et réapparaitre le monstre
            self.rect.x = random.randint(-10, 500)
            self.velocity = random.randint(1, self.default_speed)
            self.rect.y = -15
            self.health = self.max_health
            # adding score
            self.game.addscore(self.score_value)

            # si la barre d'évenement est chargé au maxium
            if self.game.comet_event.is_full_loaded():
                # retirer les monstre du jeu
                self.game.all_asteroides.remove(self)

                # appel de la méthode pour essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()




    def forward(self):
        # le déplacement ne se fait que s'il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
            self.rotation()
            # si le joueur est en collision avec le joueur
        else:
            # infliger des dégats ( au joeur)
            self.game.sound_manager.playsound('explosion')
            self.game.player.damage(self.attack)

        # si l'astéroide à traversé l'écran
        if self.rect.y >= 810:
            self.rect.x = random.randrange(-10, 500)
            self.rect.y = -15
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)





    def update_health_bar(self, surface):
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


# définir une classe pour le big asteroide
class Big_Asteroide(Asteroide):
    def __init__(self, game):
        super().__init__(game, 'img/asteroide/meteorBrown_big2.png', 30)
        self.health = 180
        self.max_health = 160
        self.attack = 0.2
        self.image = pygame.transform.scale(self.image, (150, 120))
        self.set_speed(2)




# définir une class pour l'astéroide médium
class Med_Asteroide(Asteroide):

    def __init__(self, game):
        super().__init__(game, 'img/asteroide/meteorBrown_big1.png', 20)
        self.set_speed(4)


# définir une classe pour l'astéroide petit
class Small_Asteroide(Asteroide):

    def __init__(self,game ):
        super().__init__(game, 'img/asteroide/meteorBrown_small1.png', 10)
        self.health = 20
        self.max_health = 20
        self.attack = 0.05
        self.set_speed(5)




