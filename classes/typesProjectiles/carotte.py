import random
import pygame
from classes.projectile import Projectile

class Carotte(Projectile): # Apparait sur les bords de l'écran, puis lance un laser
    def __init__(self, difficulty, image):
        super(Projectile, self).__init__()
        self.difficulty = difficulty
        self.velocity = 1
        self.pointDeDepart = random.randint(0, 3)
        self.angle = 90 * self.pointDeDepart
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 134))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.time = 0 # Permets de savoir quand il va commencer son laser
        self.rect_init()

    def rect_init(self): # A modifier chez les classes filles si nous voulons changer l'emplacement des points de spawn
        if self.pointDeDepart == 0:  # part d'en bas 
            self.rect.x = random.randint(0, 1024 - self.rect.w) 
            self.rect.y = 768 
            self.bar_position = [self.rect.x + self.rect.w / 2 - 5, 0, 10, self.rect.y - self.rect.h / 2]
        elif self.pointDeDepart == 1:  # part de droite
            self.rect.x = 1024 
            self.rect.y = random.randint(0, 768 - self.rect.h) 
            self.bar_position = [0, self.rect.y + self.rect.h / 2 - 5, self.rect.x - self.rect.w / 2, 10]
        elif self.pointDeDepart == 2:  # part d'en haut
            self.rect.x = random.randint(0, 1024 - self.rect.w) 
            self.rect.y = 0 - self.rect.h
            self.bar_position = [self.rect.x + self.rect.w / 2, 0 + self.rect.h / 2 - 5, 10, 768]
        elif self.pointDeDepart == 3:  # part de gauche
            self.rect.x = 0 - self.rect.w
            self.rect.y = random.randint(0, 768 - self.rect.h) 
            self.bar_position = [0 + self.rect.w / 2, self.rect.y + self.rect.h / 2 - 5, 1024, 10]

    def move(self):
        if self.time > 180:
            print(self.time)
            if self.pointDeDepart == 0:
                self.rect.y += self.velocity
            elif self.pointDeDepart == 1:
                self.rect.x += self.velocity
            elif self.pointDeDepart == 2:
                self.rect.y -= self.velocity
            elif self.pointDeDepart == 3:
                self.rect.x -= self.velocity
        elif self.time < 60:
            if self.pointDeDepart == 0:
                self.rect.y -= self.velocity
            elif self.pointDeDepart == 1:
                self.rect.x -= self.velocity
            elif self.pointDeDepart == 2:
                self.rect.y += self.velocity
            elif self.pointDeDepart == 3:
                self.rect.x += self.velocity
        self.time += 1