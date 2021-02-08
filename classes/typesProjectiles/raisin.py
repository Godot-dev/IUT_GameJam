import random
import pygame
from classes.projectile import Projectile

class Raisin(Projectile): # la pomme se déplace en ligne droite, de taille 64x64, de vitesse moyenne
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = pygame.image.load("assets/raisin.png")
        self.image = pygame.transform.scale(self.image, (57, 64))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect_init()