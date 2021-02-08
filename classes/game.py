import pygame
from classes.cauchemar import Cauchemar

class Game:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/1.png')
        self.is_playing = False
        self.pressed = {} # Représente les touches actuellement enfoncées par le joueur
        self.etape = 1 # 1 représente le premier jour, 2 le deuxième, 3 le troisième, et les suivants représentent les cinématiques de fin
        self.jour = False # indique s'il fait jour ou nuit, au début du jeu, on est sur la phase Jour 
        self.phaseDeJeu = None

    def drawJeu(self,screen):
        screen.blit(self.background, (0, 0))
        if not self.jour and self.phaseDeJeu == None:
            self.phaseDeJeu = Cauchemar(self.etape, self.phaseDeJeu)
        elif not self.jour:
            self.phaseDeJeu.drawCauchemar(screen, self.pressed)

    def catch_signal(self):
        # On effectue les actions du jeu en fonction de l'endroit où nous sommes
        if not self.jour and self.phaseDeJeu != None:
            self.phaseDeJeu.catch_signal(self.pressed)