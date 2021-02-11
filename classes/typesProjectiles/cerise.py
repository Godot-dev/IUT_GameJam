import random
import pygame
from classes.projectile import Projectile

class Cerise(Projectile): # La cerise commence tout droit puis fait un virage à mi-parcourt
    def __init__(self, difficulty, image):
        super(Projectile, self).__init__()
        self.difficulty = difficulty
        self.velocity = 3 + difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.firstStep = True # Passera à False quand la cerise commencera son angle
        self.direction = random.randint(0,1)
        if self.direction == 0: # on veut que self.direction soit égal à -1 ou 1 aléatoirement
            self.direction = -1
        self.rect_init()

    def rect_init(self): # A modifier chez les classes filles si nous voulons changer l'emplacement des points de spawn
        if self.pointDeDepart == 0:  # part d'en bas 
            self.rect.x = 512 - self.rect.w / 2
            self.rect.y = 768 + self.rect.h
        elif self.pointDeDepart == 1:  # part de droite
            self.rect.x = 1024
            self.rect.y = 384 - self.rect.h/2
        elif self.pointDeDepart == 2:  # part d'en haut
            self.rect.x = 512 - self.rect.w / 2
            self.rect.y = 0 - self.rect.h
        elif self.pointDeDepart == 3:  # part de gauche
            self.rect.x = 0 - self.rect.w
            self.rect.y = 384 - self.rect.h/2

    def move(self): 
        if self.pointDeDepart == 0:
            if self.firstStep == True and self.rect.y > 384 - self.rect.h/2: # Pour faire un virage pile au milieu
                self.rect.y -= self.velocity
            elif self.firstStep == False:
                self.rect.x += self.velocity * self.direction
            else:
                self.firstStep = False
        elif self.pointDeDepart == 1:
            if self.firstStep == True and self.rect.x > 512 - self.rect.w/2:
                self.rect.x -= self.velocity
            elif self.firstStep == False:
                self.rect.y += self.velocity * self.direction
            else:
                self.firstStep = False
        elif self.pointDeDepart == 2:
            if self.firstStep == True and self.rect.y < 384 - self.rect.h/2:
                self.rect.y += self.velocity
            elif self.firstStep == False:
                self.rect.x -= self.velocity * self.direction
            else:
                self.firstStep = False
        elif self.pointDeDepart == 3:
            if self.firstStep == True and self.rect.x < 512 - self.rect.w/2:
                self.rect.x += self.velocity
            elif self.firstStep == False:
                self.rect.y -= self.velocity * self.direction
            else:
                self.firstStep = False