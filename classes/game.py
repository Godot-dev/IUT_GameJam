import pygame
from classes.cauchemar import Cauchemar

class Game:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/1.png')
        self.is_playing = False
        self.pressed = {} # Représente les touches actuellement enfoncées par le joueur
        self.etape = 1 # 1 représente le premier jour


    def drawJeu(self,screen):
        screen.blit(self.background, (0, 0))
        if self.etape % 2 == 0 and self.cauchemar == None:
            self.cauchemar = Cauchemar(self.etape, self.visualNovelPart)
        elif self.etape % 2 == 0:
            self.cauchemar.drawCauchemar(screen)

    def catch_signal(self,event):
        # On mets à jour pressed
        if event.type == pygame.KEYDOWN:
            self.pressed[event.key] = True
        if event.type == pygame.KEYUP:
            self.pressed[event.key] = False

        # On effectue les actions du jeu en fonction de l'endroit où nous sommes
        if self.etape % 2 == 0 and self.cauchemar != None:
            self.cauchemar.catch_signal(self.pressed)