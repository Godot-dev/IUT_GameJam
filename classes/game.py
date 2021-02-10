import pygame
from classes.cauchemar import Cauchemar
from classes.visualNovel import VisualNovel

class Game:
    def __init__(self):
        # Image de background
        self.is_playing = False
        self.pressed = {} # Représente les touches actuellement enfoncées par le joueur
        self.etape = 1 # 1 représente le premier jour, 2 le deuxième, 3 le troisième, et les suivants représentent les cinématiques de fin
        self.jour = True # indique s'il fait jour ou nuit, au début du jeu, on est sur la phase Jour 
        self.phaseDeJeu = None

    def drawJeu(self,screen,display):
        if self.jour and self.phaseDeJeu == None:
            self.phaseDeJeu = VisualNovel("assets/novels/test.json", screen, display)
        if not self.jour and self.phaseDeJeu == None:
            self.phaseDeJeu = Cauchemar(self.etape, self.phaseDeJeu, self)
        if not self.jour:
            self.phaseDeJeu.drawCauchemar(screen)

    def catch_signal(self, event):
        # On effectue les actions du jeu en fonction de l'endroit où nous sommes
        if self.jour:
            if self.phaseDeJeu.catch_signal(self.pressed, event):
                self.jour = False
                self.phaseDeJeu = None
        else:
            self.phaseDeJeu.catch_signal(self.pressed)