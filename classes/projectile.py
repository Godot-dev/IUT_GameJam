import random
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3
        self.pointDeDepart = random.randint(0, 3) # Indique si on part d'en bas de l'écran, à gauche de l'écran etc...
        self.angle = 90 * self.pointDeDepart
        self.rect_init()

    def rect_init(self):
        if self.pointDeDepart == 0:  # part d'en bas 
            self.rect.x = random.randint(0, 1024)
            self.rect.y = 768
        elif self.pointDeDepart == 1:  # part de droite
            self.rect.x = 1024
            self.rect.y = random.randint(0, 768)
        elif self.pointDeDepart == 2:  # part d'en haut
            self.rect.x = random.randint(0, 1024)
            self.rect.y = 0
        elif self.pointDeDepart == 3:  # part de gauche
            self.rect.x = 0
            self.rect.y = random.randint(0, 768)

    def move(self): # A faire hériter aux classes filles pour modifier les patterns
        if self.pointDeDepart == 0:
            self.rect.y -= self.velocity
        elif self.pointDeDepart == 1:
            self.rect.x -= self.velocity
        elif self.pointDeDepart == 2:
            self.rect.y += self.velocity
        elif self.pointDeDepart == 3:
            self.rect.x += self.velocity
        
    def supprimer(self):
        self.cauchemar.liste_projectiles.remove(self)
        