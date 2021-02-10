import random
import pygame
from classes.projectile import Projectile

class Salade(Projectile): # la salade se déplace en diagonale, d'un angle à l'autre de l'écran
    def __init__(self, difficulty, image):
        super(Projectile, self).__init__()
        self.difficulty = difficulty
        self.velocity = 2 + difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect_init()

    def rect_init(self): # On place la salade à un des angles
        if self.pointDeDepart == 0: # Haut Gauche
            self.rect.x = 0 - self.rect.w
            self.rect.y = 0 - self.rect.h
        elif self.pointDeDepart == 1: # Haut Droit
            self.rect.x = 1024
            self.rect.y = 0 - self.rect.h
        elif self.pointDeDepart == 2: # Bas Gauche 
            self.rect.x = 0 - self.rect.w
            self.rect.y = 768
        elif self.pointDeDepart == 3: # Bas Droit
            self.rect.x = 1024
            self.rect.y = 768
        


    def move(self): # On redéfinit move pour se déplacer en diagonale
        if self.pointDeDepart == 0:
            self.rect.y += self.velocity
            self.rect.x += self.velocity
        elif self.pointDeDepart == 1:
            self.rect.x -= self.velocity
            self.rect.y += self.velocity
        elif self.pointDeDepart == 2:
            self.rect.y += self.velocity
            self.rect.x -= self.velocity
        elif self.pointDeDepart == 3:
            self.rect.x -= self.velocity
            self.rect.y -= self.velocity

