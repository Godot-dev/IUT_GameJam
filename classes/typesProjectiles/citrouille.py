import random
import pygame
from classes.projectile import Projectile

class Citrouille(Projectile): # la pomme se déplace en ligne droite, de taille 64x64, de vitesse moyenne
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3 + cauchemar.difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = pygame.image.load("assets/citrouille.png")
        self.image = pygame.transform.scale(self.image, (165, 150))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect_init()

    def rect_init(self): # A modifier chez les classes filles si nous voulons changer l'emplacement des points de spawn
        if self.pointDeDepart == 0:  # part d'en bas 
            self.rect.x = random.randint(10, 859)
            self.rect.y = 768
        elif self.pointDeDepart == 1:  # part de droite
            self.rect.x = 1024
            self.rect.y = random.randint(10, 708)
        elif self.pointDeDepart == 2:  # part d'en haut
            self.rect.x = random.randint(10, 859)
            self.rect.y = 0
        elif self.pointDeDepart == 3:  # part de gauche
            self.rect.x = 0
            self.rect.y = random.randint(10, 708)