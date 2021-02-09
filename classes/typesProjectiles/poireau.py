import random
import pygame
from classes.projectile import Projectile

class Poireau(Projectile): # Le poireau avance en ligne droite jusqu'au milieur de l'écran puis fait demi-tour
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3 + cauchemar.difficulty
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = pygame.image.load("assets/poireau.png")
        self.image = pygame.transform.scale(self.image, (64, 108))
        self.rotation = 0
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.firstStep = True # Passera à False quand le poireau commencera son demi-tour
        self.rect_init()

    def move(self): # A modifier si chez les classes filles pour modifier les patterns de déplacement
        # self.image = pygame.transform.rotate(self.image, self.rotation)
        # self.rotation += 6
        if self.pointDeDepart == 0:
            if self.firstStep == True and self.rect.y > 330: # 768/2 - 108/2
                self.rect.y -= self.velocity
            elif self.firstStep == False:
                self.rect.y += self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 1:
            if self.firstStep == True and self.rect.x > 458: # 1024/2 - 108/2
                self.rect.x -= self.velocity
            elif self.firstStep == False:
                self.rect.x += self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 2:
            if self.firstStep == True and self.rect.y < 330: # 768/2 - 108/2
                self.rect.y += self.velocity
            elif self.firstStep == False:
                self.rect.y -= self.velocity
            else:
                self.firstStep = False
                self.velocity += 2
        elif self.pointDeDepart == 3:
            if self.firstStep == True and self.rect.x < 458: # 1024/2 - 108/2
                self.rect.x += self.velocity
            elif self.firstStep == False:
                self.rect.x -= self.velocity
            else:
                self.firstStep = False
                self.velocity += 2