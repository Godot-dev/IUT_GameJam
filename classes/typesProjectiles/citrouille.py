import random
import pygame
from classes.projectile import Projectile

class Citrouille(Projectile): # la pomme se déplace en ligne droite, de taille 64x64, de vitesse moyenne
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        #self.velocity = 3
        #self.pointDeDepart = random.randint(0, 3)
        #self.angle = 90 * self.pointDeDepart
        self.image = pygame.image.load("assets/banane.png")
        self.image = pygame.transform.scale(self.image, (140, 128))
        #self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect_init()
        self.cooldown = 0 # Permets d'atteindre deux secondes avant son apparition 

    def rect_init(self):
        self.rect.x = random.randint(10, 886)
        self.rect.y = random.randint(10,630)

    def move(self):
        if self.cooldown == 120:
            self.image = pygame.image.load("assets/citrouille.png")
            self.image = pygame.transform.scale(self.image, (140, 128))
        elif self.cooldown > 240:
            self.supprimer()
        self.cooldown += 1