import random
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3
        self.direction = random.randint(0, 3)
        self.angle = 90 * self.direction
        self.rect_init()

    def rect_init(self):
        if self.direction == 0:  # part d'en haut
            self.rect.y = 768
            self.rect.x = random.randint(0, 1024)
        elif self.direction == 1:  # part de gauche
            self.rect.x = 1024
            self.rect.y = random.randint(0, 768 - self.rect.height)
        elif self.direction == 2:  # part d'en bas
            self.rect.y = - self.rect.y
            self.rect.x = random.randint(0, 1024)
        elif self.direction == 3:  # part de droite
            self.rect.x = - self.rect.width
            self.rect.y = random.randint(0, 768 - self.rect.height)

    def move(self): # A faire hériter aux classes filles pour modifier les patterns
        if self.direction == 0:
            self.rect.y -= self.velocity
        elif self.direction == 1:
            self.rect.x -= self.velocity
        elif self.direction == 2:
            self.rect.y += self.velocity
        elif self.direction == 3:
            self.rect.x += self.velocity
        
    def nettoyage(self):
        self.cauchemar.liste_projectiles.remove(self)
        