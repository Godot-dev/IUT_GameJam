import random
import pygame
from classes.projectile import Projectile

class Radis(Projectile): # Le radis se déplace en ligne droite, mais beaucoup plus rapidement que les autres fruits et légumes
    def __init__(self, difficulty, image):
        super(Projectile, self).__init__()
        self.difficulty = difficulty
        self.velocity = 4 + 2 * difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect_init()