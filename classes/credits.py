import pygame
from classes.button import Button

class Credits:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/Crédit.png')
        self.menu =    Button(260, 107, 382, 650, 'assets/M.png')
        # Instanciation des éléments liés au menu des options
        self.is_credits = False

    def drawCredits(self,screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.menu.img, self.menu.hitbox)
        

    def catch_signal(self,event):
     

        if self.menu.hitbox.collidepoint(event.pos):
            self.is_credits = False
        

