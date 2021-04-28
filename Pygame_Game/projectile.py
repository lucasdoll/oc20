import pygame

# définit la classe qui va gérer le projectile de notre jeu
class Projectile(pygame.sprite.Sprite):
    # définir le constructeur de cettte classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('img/shoot/blue_lazer.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 117
        self.rect.y = player.rect.y - 55


    def move(self):
        self.rect.y -= self.velocity

        #verifier si le projectile n'est plus sur l'ecran
        if self.rect.y < -20:
            # suprimmer le projectile( en dehors de l'ecran)
            self.player.all_projectiles.remove(self)

        # vérifier si le projectile rentre en collision avec le joueur
        for asteroide in self.player.game.check_collision(self, self.player.game.all_asteroides):
            # supprimer le projectils
            self.remove()
            # infliger des dégats
            asteroide.damage((self.player.attack))

    def projectile_enemy(self):
        self.rect.y += self.velocity

        #verifier si le projectile n'est plus sur l'ecran
        if self.rect.y < -20:
            # suprimmer le projectile( en dehors de l'ecran)
            self.player.all_projectiles.remove(self)

        # vérifier si le projectile rentre en collision avec le joueur
        for player in self.player.game.check_collision(self, self.player.game.all_asteroides):
            # supprimer le projectils
            self.remove()
            # infliger des dégats
            player.damage((self.player.attack))



    def remove(self):
        self.player.all_projectiles.remove(self)

