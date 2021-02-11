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
        self.legumesFruits = []
        self.perdu = False # Passe à true si le joueur meurt pendant le cauchemar
        self.finCauchemar = False
        self.music = False

    def drawJeu(self,screen,display):
        if self.perdu and self.phaseDeJeu == None:
            if self.music == False:
                music = True
                pygame.mixer.music.load("assets/music/themeHome/Rio_Bravo_Home.ogg")
                pygame.mixer.music.play()
            print(f"assets/novels/defaiteDay{self.etape}.json")
            self.jour = True
            self.phaseDeJeu = VisualNovel(f"assets/novels/defaiteDay{self.etape}.json", screen, display)

        elif not self.perdu and self.jour and self.phaseDeJeu == None:
            if self.music == False:
                pygame.mixer.music.load("assets/music/mainTheme/Who_Shot_Liberty_Valance.ogg")
                pygame.mixer.music.play()
                self.music = True
            self.phaseDeJeu = VisualNovel(f"assets/novels/day{self.etape}.json", screen, display)
        elif not self.jour and self.phaseDeJeu == None:
            if self.music == False:
                pygame.mixer.music.load(f"assets/music/Nightmare/nightmare{self.etape}.ogg")
                pygame.mixer.music.play()
                self.music = True
            self.phaseDeJeu = Cauchemar(self.etape, self.legumesFruits, self)
        elif not self.jour and not self.finCauchemar:
            self.phaseDeJeu.drawCauchemar(screen)

    def catch_signal(self, event):
        # On effectue les actions du jeu en fonction de l'endroit où nous sommes
        if self.jour:
            if self.phaseDeJeu.catch_signal(self.pressed, event): # Fin dialogue
                self.legumesFruits = self.phaseDeJeu.listValeurs # On passe la liste des choix au futur cauchemar
                self.jour = False
                self.phaseDeJeu = None
                self.music = False
                if self.perdu: # Le joueur a perdu et la cinématique de défaite est terminée
                    self.is_playing = False
        elif self.finCauchemar:
            self.etape += 1
            self.jour = True
            self.finCauchemar = False
            self.music = False
        elif not self.perdu:
            self.phaseDeJeu.catch_signal(self.pressed)
        
            