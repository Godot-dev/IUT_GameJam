import random
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, cauchemar):
        super(Projectile, self).__init__()
        self.cauchemar = cauchemar
        self.velocity = 3

    def rect_init(self): # A modifier chez les classes filles si nous voulons changer l'emplacement des points de spawn
        if self.pointDeDepart == 0:  # part d'en bas 
            self.rect.x = random.randint(0, 1024 - self.rect.w)
            self.rect.y = 768 + self.rect.h
        elif self.pointDeDepart == 1:  # part de droite
            self.rect.x = 1024
            self.rect.y = random.randint(0, 768 - self.rect.h)
        elif self.pointDeDepart == 2:  # part d'en haut
            self.rect.x = random.randint(0, 1024 - self.rect.w)
            self.rect.y = 0 - self.rect.h
        elif self.pointDeDepart == 3:  # part de gauche
            self.rect.x = 0 - self.rect.w
            self.rect.y = random.randint(0, 768 - self.rect.h)

    def move(self): # A modifier si chez les classes filles pour modifier les patterns de déplacement
        if self.pointDeDepart == 0:
            self.rect.y -= self.velocity
        elif self.pointDeDepart == 1:
            self.rect.x -= self.velocity
        elif self.pointDeDepart == 2:
            self.rect.y += self.velocity
        elif self.pointDeDepart == 3:
            self.rect.x += self.velocity
        
    def supprimer(self):
        print("a")
        self.cauchemar.liste_projectiles.remove(self)
        