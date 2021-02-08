from classes.cauchemar import Cauchemar
import pygame
from classes.cauchemar import Cauchemar

class Game:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/1.png')
        self.is_playing = False
        self.pressed = {} # Représente les touches actuellement enfoncées par le joueur
        self.etape = 2 # 1, 3 et 5 sont les étapes jour, et les cauchemars sont aux étapes 2, 4 et 6. 7 et 8 correspondent aux deux fins
        self.cauchemar = None
        self.visualNovelPart = None


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