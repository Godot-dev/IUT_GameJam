import random
import pygame
from classes.projectile import Projectile

class Banane(Projectile): # la salade se déplace en diagonale, de taille 64x64, de vitesse moyenne
    def __init__(self, cauchemar, image):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 2 + cauchemar.difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.direction = random.randint(0, 1) # Indique si la salade ira en diagonale vers sa gauche ou vers sa droite
        if self.direction == 0: # On a besoin que self.direction soit égal à 1 ou -1, pas 0
            self.direction = -1
        self.i = 1
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 133))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect_init()


    def move(self): # On redéfinit move pour se déplacer en diagonale
        self.i += 1
        if self.i == 60:
            self.direction *= -1
            self.i = 1
        if self.pointDeDepart == 0:
            self.rect.y -= self.velocity
            self.rect.x += self.velocity * self.direction
        elif self.pointDeDepart == 1:
            self.rect.x -= self.velocity
            self.rect.y += self.velocity * self.direction
        elif self.pointDeDepart == 2:
            self.rect.y += self.velocity
            self.rect.x += self.velocity * self.direction
        elif self.pointDeDepart == 3:
            self.rect.x += self.velocity
            self.rect.y += self.velocity * self.direction