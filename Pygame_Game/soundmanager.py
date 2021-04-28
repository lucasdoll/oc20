import pygame

class Soundmanager:

    def __init__(self):
        self.sounds ={
            'click': pygame.mixer.Sound('music/click.mp3'),
            'explosion': pygame.mixer.Sound('music/explosion.mp3'),
            'lazer': pygame.mixer.Sound('music/lazer.mp3'),
        }

    def playsound(self, name):
        self.sounds[name].play()
