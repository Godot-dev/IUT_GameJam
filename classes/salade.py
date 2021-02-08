import random
import pygame
from classes.projectile import Projectile

class Salade(Projectile): # la salade se déplace en diagonale, de taille 64x64, de vitesse moyenne
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 2
        self.direction = random.randint(0, 3)
        self.angle = 90 * self.direction
        self.image = pygame.image.load("assets/bowling-ball.png")
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect_init()

    def move(): # On redéfinit move pour se déplacer en diagonale
