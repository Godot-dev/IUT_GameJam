import random
import pygame
from classes.projectile import Projectile

class Raisin(Projectile): # Le raisin est très lent, ce qui augmente la fréquence d'ennemis à l'écran
    def __init__(self, difficulty, image):
        super(Projectile, self).__init__()
        self.difficulty = difficulty
        self.velocity = 2 
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect_init()
        self.miniRaisin = pygame.image.load("assets/projectiles/miniRaisin.png")
        self.miniRaisinRect = self.miniRaisin.get_rect()


    # def rect_init(self): # A modifier chez les classes filles si nous voulons changer l'emplacement des points de spawn
    #     if self.pointDeDepart == 0:  # part d'en bas 
    #         self.rect.x = 512 - self.rect.w / 2
    #         self.rect.y = 768 + self.rect.h
    #     elif self.pointDeDepart == 1:  # part de droite
    #         self.rect.x = 1024
    #         self.rect.y = 384 - self.rect.h/2
    #     elif self.pointDeDepart == 2:  # part d'en haut
    #         self.rect.x = 512 - self.rect.w / 2
    #         self.rect.y = 0 - self.rect.h
    #     elif self.pointDeDepart == 3:  # part de gauche
    #         self.rect.x = 0 - self.rect.w
    #         self.rect.y = 384 - self.rect.h/2

    
