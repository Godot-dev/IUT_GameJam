import pygame

class Button:
    def __init__(self, width, height, posx, posy, img):
        # Instanciation du bouton avec ses différents paramètres
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (width, height)) # On redimensionne
        self.hitbox = self.img.get_rect() # On implémente la hitbox du bouton
        self.hitbox.x = posx
        self.hitbox.y = posy