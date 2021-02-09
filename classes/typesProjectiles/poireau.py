import random
import pygame
from classes.projectile import Projectile

class Poireau(Projectile): # Le poireau avance en ligne droite jusqu'au milieur de l'écran puis fait demi-tour
    def __init__(self, cauchemar, image):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3 + cauchemar.difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 108))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.firstStep = True # Passera à False quand le poireau commencera son demi-tour
        self.rect_init()

    def move(self): 
        if self.pointDeDepart == 0:
            if self.firstStep == True and self.rect.y > 384 - self.rect.h/2: # Pour faire demi tour pile au milieu
                self.rect.y -= self.velocity
            elif self.firstStep == False:
                self.rect.y += self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 1:
            if self.firstStep == True and self.rect.x > 512 - self.rect.w/2:
                self.rect.x -= self.velocity
            elif self.firstStep == False:
                self.rect.x += self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 2:
            if self.firstStep == True and self.rect.y < 384 + self.rect.h/2:
                self.rect.y += self.velocity
            elif self.firstStep == False:
                self.rect.y -= self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 3:
            if self.firstStep == True and self.rect.x < 512 + self.rect.w/2:
                self.rect.x += self.velocity
            elif self.firstStep == False:
                self.rect.x -= self.velocity
            else:
                self.firstStep = False
                self.velocity += 2